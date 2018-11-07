# Rex API

This repository illustrates how to use the Rex API. The Python file is a simple desktop application with command line input.

## Endpoints, input and responses

The API currently offers 2 endpoints: One to get the OAuth token (valid 60 minutes) and one to perform the actual message request:

- https://meetrex.com/token
- https://meetrex.com/api/review-requests

The token endpoint returns a JSON object like the following:

{"access_token":"G6Nj92l4SRXDE9b4VKKQADDhy_3HobdE4T8rf6Pg42xGpa0NDOZzwCbiZf_4128tHTgjMVCpL0JsTAHLiaCQCVNACeE4eIHyzB4rdJiqea6ReDlUUoTVo1HjiTB6o9vNbRzqukDk9qFQiq2j3eHkJRFctC7jlhl53sz6mD5BDX7bY_CNSv_FvbdTX6HJOLbnlma72RRko9eiUn2TNOL4qs_a3GWa_C1XRoQXG6P0Tw4QAvDX1540bEjqy8tnOdKFVGaKErhcgPrqfOXVVKFPyV0tNgPS_a8Nk3Xfe8a9pq7W_6qnJo93kR_5vJhFwQ8a84QtwOCxM-0vyqQ-kgdRMqeg2viKjEPckRmxjTD0T7jrMaC97_LVhqLfPS5RhpkvU1VSv0rm-z_3xCwSdeJZ-DDRH5WOPNtz2yib0j51wNe3UocO-MGqCgrkf9ZP24jxsL-RjK6kxg8M-vPTGpFg8GSGF8nLBri8239h4QSn7AH23xy-AIfr1ntrsOMfp2GRaPSXjuuV-N56rgDFuCGiJg","token_type":"bearer","expires_in":3599,"userName":"person@example.com",".issued":"Wed, 07 Nov 2018 04:17:34 GMT",".expires":"Wed, 07 Nov 2018 05:17:34 GMT"}

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

