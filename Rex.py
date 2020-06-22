import json
import requests

# API endpoints
tokenUrl = "https://meetrex.com/token"
messageUrl = "https://meetrex.com/api/review-requests"

# User input
username = input("Enter your Rex username: ")
password = input("Enter your password: ")
# Number of the account to be used. Can be omitted if user has only one account.
account = input("Enter your account number: ")
# Account identifier string. Can be omitted if user has only one account. Will be ignored if account number is entered.
accountID = input("Enter your account identifier: ")
name = input("Enter the recipient's name: ")
salutation = input('Enter how you want to address the recipient (ex.: "Mrs. Smith"): ')
# Either email or phone is required, using both is possible
email = input("Enter the recipient's email: ")
phone = input("Enter the recipient's mobile phone number: ")

# Get OAuth token
authentication = "username=" + username + "&password=" + password + "&grant_type=password"
authResponse = requests.post(tokenUrl, data=authentication)
if authResponse.status_code == 200:
	jsonResponse = json.loads(authResponse.content)
	token = jsonResponse["access_token"]
	
	data = [ { "OwnerID": account, "AccountIdentifier": accountID, "Name": name, "Salutation": salutation, "Phone": phone, "Email": email } ]
	headers = { "Authorization": "Bearer " + token, "Content-Type": "application/json" }
	# Send Rex message
	messageResponse = requests.post(messageUrl, json=data, headers=headers)
	if messageResponse.status_code == 201:
		print("Message sent")
	else:
		print("Sending failed with status code " + str(messageResponse.status_code))
else:
	print("Authorization failed with status code " + str(authResponse.status_code))

input("Press Enter to close this window.")