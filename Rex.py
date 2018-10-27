import json
import requests

# API endpoints
tokenUrl = "https://meetrex.com/token"
messageUrl = "https://meetrex.com/api/review-requests"

# User input
username = input("Enter your Rex username: ")
password = input("Enter your password: ")
name = input("Enter the recipient's name: ")
# Either email or phone is required, using both is possible
email = input("Enter the recipient's email: ")
phone = input("Enter the recipient's 10-digit cell phone number: ")

# Get OAuth token
authentication = "username=" + username + "&password=" + password + "&grant_type=password"
authResponse = requests.post(tokenUrl, data=authentication)
if authResponse.status_code == 200:
	jsonResponse = json.loads(authResponse.content)
	token = jsonResponse["access_token"]
	
	data = [ { "Name": name, "Phone": phone, "Email": email } ]
	headers = { "Authorization": "Bearer " + token, "Content-Type": "application/json" }
	# Send Rex message
	messageResponse = requests.post(messageUrl, json=data, headers=headers)
	if messageResponse.status_code == 201:
		print("Message sent")
	else:
		print("Sending failed with status code " + str(messageResponse.status_code))
else:
	print("Authorization failed with status code " + str(authResponse.status_code))