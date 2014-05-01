import requests
import hashlib
import json

from function import *

##### Global variables #####
url_root = 'http://0.0.0.0:8008/client/'
key = None
session_id = 0
session = 0
balance = 0

##### Key exchange #####

# Data send to Key exchange:
# send_data = {'publicKey': publicKey}
# publicKey: the client publicKey for server to obtain crypto key
#
# Data received from Key exchange:
# received_data = {"is_session": is_session, "expire": expire, "data": data, }
# is_session: a boolean shows the session is set up or not
# expire: a boolean shows the session is expired or not
# data: plaintext, if session is not created, data = None
# data = {'session_id': session_id, 'publicKey': publicKey, }
# session_id: the id of the session
# publicKey: the server publicKey to obtain crypto key

# Get client public key
crypto = DiffieHellman()
send_data = {'publicKey': str(crypto.publicKey)}

# Get server public key and session id
receive = requests.post(url_root + 'key/exchange/', send_data)
received_data = json.loads(receive.text)

serverKey = long(received_data["publicKey"])
session_id = received_data["session_id"]

# Get crypto key
crypto.genKey(serverKey)
crypto.getKey()
key = hexlify(crypto.key)

##### User login #####
# Data send to Key exchange:
# send_data = {"data": data, 'session_id': session_id}
# session_id: the id of session
# data: cipher text
# data = {'username': username, 'password': password, }
# username: email of user
# password: hashed password
#
# Data received from User login:
# received_data = {"is_session": is_session, "expire": expire, "data": data, }
# is_session: a boolean shows the session is set up or not
# expire: a boolean shows the session is expired or not
# data: plaintext, if session is not created, data = None
# data = {"success": success, "session": session}
# success: a boolean shows login success or not
# session: the number of session


# Get username and password
# username = raw_input("Please enter username: ")
# password = raw_input("Please enter password: ")
username = "yunsheng@umass.edu"
password = "yunsheng22"
hash_password = hashlib.sha1(password).hexdigest()
data = {'username': username, 'password': hash_password, }

# Encrypt data
bin_data = encrypt(data, key)

# Request session number and login
send_data = {"data": bin_data, 'session_id': session_id}
receive = requests.post(url_root + 'request/new/session/', send_data)
received_data = json.loads(receive.text)
data = decrypt(received_data["data"], key)

session = data["session"]
balance = data['balance']

if data['success']:
    print session
    print balance

##### Request service #####
