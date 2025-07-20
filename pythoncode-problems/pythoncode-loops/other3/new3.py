import requests

# Authorization token (replace with valid one)
auth_token = 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjFBRjQzNjk5RUE0NDlDNkNCRUU3NDZFMjhDODM5NUIyMEE0MUNFMTgiLCJ4NXQiOiJHdlEybWVwRW5HeS01MGJpaklPVnNncEJ6aGciLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FwcC5rZWthLmNvbSIsIm5iZiI6MTc0MjMxMzc0MSwiaWF0IjoxNzQyMzEzNzQxLCJleHAiOjE3NDI0MDAxNDEsImF1ZCI6WyJrZWthaHIuYXBpIiwiaGlyby5hcGkiLCJodHRwczovL2FwcC5rZWthLmNvbS9yZXNvdXJjZXMiXSwic2NvcGUiOlsib3BlbmlkIiwia2VrYWhyLmFwaSIsImhpcm8uYXBpIiwib2ZmbGluZV9hY2Nlc3MiXSwiYW1yIjpbImV4dGVybmFsIl0sImNsaWVudF9pZCI6Ijk4N2NjOTcxLWZjMjItNDQ1NC05OWY5LTE2YzA3OGZhN2ZmNiIsInN1YiI6ImRmMjQ1MTlmLTVjYjMtNDBkOC1hM2JhLTExZDJkN2FhNGVlYSIsImF1dGhfdGltZSI6MTczODY4NjgyNCwiaWRwIjoiR29vZ2xlIiwidGVuYW50X2lkIjoiOTk0OTYyYTktNjcxZC00NGVkLTliZDMtNDBjNDJiZGIxMjRkIiwidGVuYW50aWQiOiI5OTQ5NjJhOS02NzFkLTQ0ZWQtOWJkMy00MGM0MmJkYjEyNGQiLCJzdWJkb21haW4iOiJmeW5kLmtla2EuY29tIiwidXNlcl9pZCI6IjFkYzJmNGYyLTkzNjUtNDk1Zi1iMDBhLTJhM2ViMjkxYWIyNiIsInVzZXJfaWRlbnRpZmllciI6IjFkYzJmNGYyLTkzNjUtNDk1Zi1iMDBhLTJhM2ViMjkxYWIyNiIsInVzZXJuYW1lIjoibW9oYW5wcmFzYWRAZ29meW5kLmNvbSIsImVtYWlsIjoibW9oYW5wcmFzYWRAZ29meW5kLmNvbSIsImF1dGhlbnRpY2F0aW9uX3R5cGUiOiIzIiwic2lkIjoiOEUwQzFBQjhCMUYwRDFFODBFODg2MjY0M0YzQUJCNkMiLCJqdGkiOiJDM0JGNUNFOEU2QTE2NkY4Q0Q1NjQyQ0Y5OUMxRTA0RSJ9.KAJIJQYkgkmQ4rVBoFYolzFEzfV3jTrTAxy3-WXGBTMa7pUAbt9ZVAHuXOi2oFg2EqdC5Iu9--QfkoUbHDFih2lZsMeh5THY3taNyFSSzxIl-H05WrfuQusXSLBGFOSvPb_-GTDvEUIB23dOKPq7iudwjxSokSIZPPV9Z6TZBLQtN6tnZr3b_WzcqyzkaDl1KXhz9kr_Y6-LzhOm5RapF1_ME39Tc4GQKNPSU74O1E-b0Ut0c62SKH3P2NJCQE4jjMXKbwLKs3YOTPTRKJ7C6bg0iKVyadmty1hABBg--FUQ7_z_XsoRFxlR6gAKAA-LqeTZmOAjVxsOnUWl11ilmw'

headers = {
    'accept': 'application/json, text/plain, */*',
    'authorization': auth_token,
    'content-type': 'application/json; charset=utf-8'
}

# List of employee IDs you want to check
employee_ids = [363977, 47383, 47405, 147111]

for emp_id in employee_ids:
    url = f'https://fynd.keka.com/k/default/api/employee/{emp_id}/profile/profileheader'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        data = json_data.get('data', {})
        name = data.get('displayName', 'N/A')
        is_onboarding_initiated = data.get('isOnboardingInitiated', None)
        print(f"Employee ID: {emp_id} | Name: {name} | isOnboardingInitiated: {is_onboarding_initiated}")
    else:
        print(f"Failed to fetch data for Employee ID: {emp_id} | Status Code: {response.status_code}")
