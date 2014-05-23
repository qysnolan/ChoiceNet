import requests
import hashlib
import json

from function import *

##### Global variables #####
url_root = 'http://0.0.0.0:8008/new/client/'
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
print "Request a new session"
print "Client public key: " + str(crypto.publicKey)

# Get server public key and session id
receive = requests.post(url_root + 'key/exchange/', send_data)
received_data = json.loads(receive.text)

serverKey = long(received_data["publicKey"])
session_id = received_data["session_id"]
print "Server public key: " + str(serverKey)
print "Session ID: " + str(session_id)

# Get crypto key
crypto.genKey(serverKey)
crypto.getKey()
key = hexlify(crypto.key)
print "Encryption key: " + key
print 

##### User login #####
# Data send to User login:
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
# data: cipher text, if session is not created, data = None
# data = {"success": success, "session": session}
# success: a boolean shows login success or not
# session: the number of session


# Get username and password
# username = raw_input("Please enter username: ")
# password = raw_input("Please enter password: ")
print "User login"
username = "yunsheng@umass.edu"
password = "yunsheng"
hash_password = hashlib.sha1(password).hexdigest()
data = {'username': username, 'password': hash_password, }
print "Password (plain text): " + password
print "Password (hashed text): " + hash_password
print "Client plain text data: " + str(data)

# Encrypt data
bin_data = encrypt(data, key)
print "Client cipher data: " + bin_data

# Request session number and login
send_data = {"data": bin_data, 'session_id': session_id}
receive = requests.post(url_root + 'request/new/session/', send_data)
received_data = json.loads(receive.text)
data = decrypt(received_data["data"], key)

session = data["session"]
balance = data['balance']
print "Server cipher data: " + str(received_data)
print "Deciphered server data: " + str(data)
print

##### Request service #####
# Data send to Request Service:
# send_data = {"data": data, 'session_id': session_id}
# session_id: the id of session
# data: cipher text
# data = {"service_id": service_id, "session": session, "amount": amount}
# service_id: the id of service request
# session: the number of session
# amount: the amount of request service (amount doesn't have any effect)
#
# Data received from Request service:
# received_data = {"is_session": is_session, "expire": expire, "data": data, }
# is_session: a boolean shows the session is set up or not
# expire: a boolean shows the session is expired or not
# data: cipher text, if session is not created, data = None
# data = {"is_service": is_service, "invoice_number": invoice_number,
#         'payment_url': payment_url}
# is_service: if service does not exist, return false
# invoice_number: the invoice of transaction
# payment_url: the url redirect user to make payment by PayPal
print "User request service"
service_id = "56-add-balance"
amount = 1

data = {"service_id": service_id, "session": session, "amount": amount}

# Encrypt data
bin_data = encrypt(data, key)
print "Client plain text data: " + str(data)
print "Client cipher data: " + bin_data

# Request service
send_data = {"data": bin_data, 'session_id': session_id}
receive = requests.post(url_root + 'request/service/', send_data)
received_data = json.loads(receive.text)
data = decrypt(received_data["data"], key)

invoice_number = data["invoice_number"]
payment_url = data["payment_url"]
print payment_url

print "Server cipher data: " + str(received_data)
print "Deciphered server data: " + str(data)
print

# Pause for waiting payment
foo = raw_input("After successful payment, enter anything: ")


##### Pay unpaid order #####
# Data send to Pay unpaid order:
# send_data = {"data": data, 'session_id': session_id}
# session_id: the id of session
# data: cipher text
# data = {"invoice_number": invoice_number, "session": session, }
# invoice_number: the order to pay
# session: the number of session
#
# Data received from Pay unpaid order:
# received_data = {"is_session": is_session, "expire": expire, "data": data, }
# is_session: a boolean shows the session is set up or not
# expire: a boolean shows the session is expired or not
# data: cipher text, if session is not created, data = None
# data = {"balance": balance, "is_invoice": is_invoice,
#         "invoice_number": invoice_number,
#         "sufficient_balance": sufficient_balance,
#         "previous_paid": previous_paid}
# balance: the new balance if transaction is not successful return -1
# is_invoice: if invoice does not exist, return false
# invoice_number: the invoice of transaction
# sufficient_balance: return True if balance is sufficient
# previous_paid: if the order is already paid, return true
# print "Pay unpaid order"
# data = {"invoice_number": invoice_number, "session": session, }
#
# # Encrypt data
# bin_data = encrypt(data, key)
# print "Client plain text data: " + str(data)
# print "Client cipher data: " + bin_data
#
# # Request service
# send_data = {"data": bin_data, 'session_id': session_id}
# receive = requests.post(url_root + 'pay/order/', send_data)
# received_data = json.loads(receive.text)
# data = decrypt(received_data["data"], key)
#
# if float(data["balance"]) >= 0:
#     balance = data["balance"]
#
# print "Server cipher data: " + str(received_data)
# print "Deciphered server data: " + str(data)
# print

##### Request refund #####
# Data send to Request refund:
# send_data = {"data": data, 'session_id': session_id}
# session_id: the id of session
# data: cipher text
# data = {"invoice_number": invoice_number, "session": session, }
# invoice_number: the order to refund
# session: the number of session
#
# Data received from Request refund:
# received_data = {"is_session": is_session, "expire": expire, "data": data, }
# is_session: a boolean shows the session is set up or not
# expire: a boolean shows the session is expired or not
# data: cipher text, if session is not created, data = None
# data = {"balance": balance, "is_invoice": is_invoice,
#         "is_refund": is_refund, }
# balance: the new balance if transaction is not successful return -1
# is_invoice: if invoice does not exist, return false
# is_refund: return false, if refund is unsuccessful
# print "Request refund"
# data = {"invoice_number": invoice_number, "session": session, }
#
# # Encrypt data
# bin_data = encrypt(data, key)
# print "Client plain text data: " + str(data)
# print "Client cipher data: " + bin_data
#
# # Request service
# send_data = {"data": bin_data, 'session_id': session_id}
# receive = requests.post(url_root + 'request/refund/', send_data)
# received_data = json.loads(receive.text)
# data = decrypt(received_data["data"], key)
#
# if float(data["balance"]) >= 0:
#     balance = data["balance"]
#
# print "Server cipher data: " + str(received_data)
# print "Deciphered server data: " + str(data)
# print