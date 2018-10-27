# Rex API

This repository illustrates how to use the Rex API. The Python file is a simple desktop application with command line input.

## Endpoints, input and responses

The API currently offers 2 endpoints: One to get the OAuth token (valid 15 minutes) and one to perform the actual message request:

- https://meetrex.com/token
- https://meetrex.com/api/review-requests

Usage can be illustrated by the cURL example below. Up to 50 messages can be sent at once. As the example shows, the phone number can be entered with or without extra characters. Email and mobile phone can both be specified, but only one is required. The only response will be the HTTP status code:

- Created: 201
- Missing or expired token: 401
- Empty or malformed json: 400
- Greater than 50 review requests: 413
- Any other server error: 500

## cURL

&lt;Rex username&gt;, &lt;password&gt; and &lt;token&gt; should be replaced with the actual username, password and the token received.

```shell
curl -i -X POST -H "Content-Type:application/x-www-form-urlencoded" https://meetrex.com/token -d 'username=<Rex username>&password=<password>&grant_type=password'

curl -i -X POST -H "Authorization: Bearer <token>" -H "Content-Type:application/json" https://meetrex.com/api/review-requests -d '[ { "Name": "Jane Doe", "Phone": "0123456789", "Email": "jane.doe@example.com" }, { "Name": "John Doe", "Phone": "(987) 654-3210", "Email": "" } ]'
```

