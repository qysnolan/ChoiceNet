import requests
import hashlib
import json

from function import *

##### Key exchange #####

# Get client public key
crypto = DiffieHellman()
data = {'publicKey': str(crypto.publicKey)}

# Get server public key and session id
receive = requests.post('http://0.0.0.0:8008/key/exchange/', data)
received_data = json.loads(receive.text)

serverKey = long(received_data["publicKey"])
session_id = received_data["session_id"]

# Get crypto key
crypto.genKey(serverKey)
crypto.getKey()
key = hexlify(crypto.key)

##### User login #####

# Get username and password
# username = raw_input("Please enter username: ")
# password = raw_input("Please enter password: ")

username = "yunsheng@umass.edu"
password = "yunsheng"
hash_password = hashlib.sha1(password).hexdigest()
data = {'username': username, 'password': hash_password}

# Encrypt data
bin_data = encrypt(data, key)

# Requst session number and login
receive = requests.post('http://0.0.0.0:8008/request/new/session/', {"data": bin_data, 'session_id': session_id})
received_data = json.loads(receive.text)
data = decrypt(received_data["data"], key)
print data["session"]


# obj2 = AES.new(key[:32])
# print obj2.decrypt(ciphertext)


# g = requests.get('http://0.0.0.0:8008/auth/login/')
# print g.text

# username = raw_input("Please enter username: ")
# password = raw_input("Please enter password: ")

# hash_password = hashlib.sha1(password).hexdigest()
# data = {'username': username, 'password': password}

# r = requests.post('http://0.0.0.0:8008/auth/login/', data)
# print r.text
# 1398891077794
# 1398891096347