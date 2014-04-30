import requests
import hashlib
from dh import *

# request new session
crypto = DiffieHellman()
data = {'publicKey': str(crypto.publicKey)}

g = requests.post('http://0.0.0.0:8008/request/new/session/', data)
serverKey = long(g.text)

crypto.genKey(serverKey)
crypto.getKey()

print "Key:", hexlify(crypto.key)

# g = requests.get('http://0.0.0.0:8008/auth/login/')
# print g.text

# username = raw_input("Please enter username: ")
# password = raw_input("Please enter password: ")

# hash_password = hashlib.sha1(password).hexdigest()
# data = {'username': username, 'password': password}

# r = requests.post('http://0.0.0.0:8008/auth/login/', data)
# print r.text