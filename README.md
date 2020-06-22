# Rex API

This repository illustrates how to use the Rex API. The Python file is a simple desktop application with command line input.

## Endpoints, input and responses

The API currently offers 3 endpoints: One to get the OAuth token (valid 60 minutes), one to perform the actual message request, and one to get a list of received referrals:

- https://meetrex.com/token (POST)
- https://meetrex.com/api/review-requests (POST)
- https://meetrex.com/api/referrals (GET)

The token endpoint returns a JSON object like the following:

{"access_token":"G6Nj92l4SRXDE9b4VKKQADDhy_3HobdE4T8rf6Pg42xGpa0NDOZzwCbiZf_4128tHTgjMVCpL0JsTAHLiaCQCVNACeE4eIHyzB4rdJiqea6ReDlUUoTVo1HjiTB6o9vNbRzqukDk9qFQiq2j3eHkJRFctC7jlhl53sz6mD5BDX7bY_CNSv_FvbdTX6HJOLbnlma72RRko9eiUn2TNOL4qs_a3GWa_C1XRoQXG6P0Tw4QAvDX1540bEjqy8tnOdKFVGaKErhcgPrqfOXVVKFPyV0tNgPS_a8Nk3Xfe8a9pq7W_6qnJo93kR_5vJhFwQ8a84QtwOCxM-0vyqQ-kgdRMqeg2viKjEPckRmxjTD0T7jrMaC97_LVhqLfPS5RhpkvU1VSv0rm-z_3xCwSdeJZ-DDRH5WOPNtz2yib0j51wNe3UocO-MGqCgrkf9ZP24jxsL-RjK6kxg8M-vPTGpFg8GSGF8nLBri8239h4QSn7AH23xy-AIfr1ntrsOMfp2GRaPSXjuuV-N56rgDFuCGiJg","token_type":"bearer","expires_in":3599,"userName":"person@example.com",".issued":"Wed, 07 Nov 2018 04:17:34 GMT",".expires":"Wed, 07 Nov 2018 05:17:34 GMT"}

The review-requests endpoint allows sending up to 50 messages at once. The API expects a JSON array of objects (see cURL examples below). The following fields are available:

- OwnerID - For users with multiple accounts. The number in the URL when you are viewing a specific Rex account. For example, if the dashboard URL is `https://meetrex.com/Owners/Details/54321`, the account number is 54321. Can be omitted if you have only one account, or if you provide an account identifier (next field).
- AccountIdentifier - For users with multiple accounts. Unique string that you use to identify this account - See Settings page, under Business Info. Ignored if account number (previous field) is provided.
- Name - The name of your customer. If no Salutation is provided, the first part of the name will be used to address your customer. For example, if the customer name is Jane Doe, the message would start with "Jane, ...". For more control, use the Salutation field.
- Salutation - How you want to address your customer. Examples: "Dear Sam", "Hi John and Jane", "Mrs. Smith". Do not add a comma. Leave blank to use the customer's first name.
- Phone - Your customer's mobile phone number. As the example shows, the phone number can be entered with or without extra characters. Email OR Phone is required.
- Email - Your customer's email address. Email OR Phone is required.

The only response will be the HTTP status code:

- Created: 201
- Missing or expired token: 401
- Empty or malformed json: 400
- Greater than 50 review requests: 413
- Any other server error: 500

The referrals endpoint returns a JSON list of referral objects, which consist of:

- "Id": Unique ID
- "OwnerID": ID of the associated Rex account
- "ResponseID": ID of the associate review request, if any
- "ReferringName": Name of the referrer
- "ReferringEmail": Referrer email address
- "ReferringPhone": Referrer phone number
- "ReferralName": Referral name
- "ReferralEmail": Referral email 
- "ReferralPhone": Referral phone number
- "ReferralDateTime": The moment at which the referral was given, in UTC

## cURL

&lt;Rex username&gt;, &lt;password&gt; and &lt;token&gt; should be replaced with the actual username, password and the token received.

```shell
curl -i -X POST -H "Content-Type:application/x-www-form-urlencoded" https://meetrex.com/token -d 'username=<Rex username>&password=<password>&grant_type=password'

curl -i -X POST -H "Authorization: Bearer <token>" -H "Content-Type:application/json" https://meetrex.com/api/review-requests -d '[ { "Name": "Jane Doe", "Phone": "0123456789", "Email": "jane.doe@example.com" }, { "Name": "John Doe", "Phone": "(987) 654-3210", "Email": "" } ]'

curl -i -H "Authorization: Bearer <token>" https://meetrex.com/api/referrals
```

