import json
import requests

# API endpoints
messageUrl = "https://meetrex.com/api/reviewrequests"

# User input
key = input("Enter your Rex API key: ")
# Number of the account to be used. Can be omitted if user has only one account.
account = input("Enter your account number: ")
# Account identifier string. Can be omitted if user has only one account. Will be ignored if account number is entered.
accountID = input("Enter your account identifier: ")
name = input("Enter the recipient's name: ")
salutation = input('Enter how you want to address the recipient (ex.: "Mrs. Smith"): ')
# Either email or phone is required, using both is possible
email = input("Enter the recipient's email: ")
phone = input("Enter the recipient's mobile phone number: ")
	
data = [ { "OwnerID": account, "AccountIdentifier": accountID, "Name": name, "Salutation": salutation, "Phone": phone, "Email": email } ]
headers = { "api-key": key, "Content-Type": "application/json" }
# Send Rex message
messageResponse = requests.post(messageUrl, json=data, headers=headers)
if messageResponse.status_code == 201:
    print("Request has been received")
else:
    print("Sending failed with status code " + str(messageResponse.status_code))

input("Press Enter to close this window.")