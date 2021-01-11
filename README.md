# Rex API

This repository illustrates how to use the Rex API. The Python file is a simple desktop application with command line input.

## Authentication

The Rex API uses key-based authentication. All requests to the API must have an 'api-key' header set. Users can generated a key [here](https://meetrex.com/Manage/ApiKeys).

## Endpoints, input and responses

The API currently offers 2 endpoints: One to perform a actual message request, and one to get a list of received referrals:

- https://meetrex.com/api/reviewrequests (POST)
- https://meetrex.com/api/referrals (GET)


The review-requests endpoint allows sending up to 50 messages at once. The API expects a JSON array of objects (see cURL examples below). The following fields are available:

- OwnerID - For users with multiple accounts. The number in the URL when you are viewing a specific Rex account. For example, if the dashboard URL is `https://meetrex.com/Owners/Details/54321`, the account number is 54321. Can be omitted if you have only one account, or if you provide an account identifier (next field).
- AccountIdentifier - For users with multiple accounts. Unique string that you use to identify this account - See Settings page, under Business Info. Ignored if account number (previous field) is provided.
- Name - The name of your customer. If no Salutation is provided, the first part of the name will be used to address your customer. For example, if the customer name is Jane Doe, the message would start with "Jane, ...". For more control, use the Salutation field.
- Salutation - How you want to address your customer. Examples: "Dear Sam", "Hi John and Jane", "Mrs. Smith". Do not add a comma. Leave blank to use the customer's first name.
- Phone - Your customer's mobile phone number. As the example shows, the phone number can be entered with or without extra characters. Email OR Phone is required.
- Email - Your customer's email address. Email OR Phone is required.

The response will be an HTTP status code:

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

&lt;key&gt; should be replaced with the user's actual API key.

```shell
curl -X POST https://meetrex.com/api/reviewrequests \
-H "api-key: <key>" \
-H "Content-Type:application/json" \
-d '[ { "Name": "Jane Doe", "Phone": "0123456789", "Email": "jane.doe@example.com" }, { "Name": "John Doe", "Phone": "(987) 654-3210", "Email": "" } ]'

curl https://meetrex.com/api/referrals \
-H "api-key: <key>" 
```

