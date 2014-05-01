from Crypto.Cipher import AES

import requests
import hashlib
import json
import binascii

from dh import *

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
IV = 16 * '\x00'
encrypt = AES.new(key[:32], AES.MODE_CFB, IV)

##### User login #####

# Get username and password
# username = raw_input("Please enter username: ")
# password = raw_input("Please enter password: ")
username = "yunsheng@umass.edu"
password = "yunsheng"
hash_password = hashlib.sha1(password).hexdigest()
print hash_password
data = {'username': username, 'password': hash_password}
json_data = json.dumps(data)

# Encrypt data
ciphertext = encrypt.encrypt(str(json_data))
bin_data = bin(int(binascii.hexlify(ciphertext), 16))

receive = requests.post('http://0.0.0.0:8008/request/new/session/', {"data": str(bin_data), 'session_id': session_id})
print receive.text


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