import requests
import hashlib

g = requests.get('http://0.0.0.0:8008/auth/login/')
print g.text

username = raw_input("Please enter username: ")
password = raw_input("Please enter password: ")

hash_password = hashlib.sha1(password).hexdigest()
data = {'username': username, 'password': password}

r = requests.post('http://0.0.0.0:8008/auth/login/', data)
print r.text