import requests
from datetime import date

# URL
url = 'https://fynd.keka.com/k/default/api/employee/lookup/globalsearch?searchKey='

# Headers
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjFBRjQzNjk5RUE0NDlDNkNCRUU3NDZFMjhDODM5NUIyMEE0MUNFMTgiLCJ4NXQiOiJHdlEybWVwRW5HeS01MGJpaklPVnNncEJ6aGciLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FwcC5rZWthLmNvbSIsIm5iZiI6MTc0MjMxMzc0MSwiaWF0IjoxNzQyMzEzNzQxLCJleHAiOjE3NDI0MDAxNDEsImF1ZCI6WyJrZWthaHIuYXBpIiwiaGlyby5hcGkiLCJodHRwczovL2FwcC5rZWthLmNvbS9yZXNvdXJjZXMiXSwic2NvcGUiOlsib3BlbmlkIiwia2VrYWhyLmFwaSIsImhpcm8uYXBpIiwib2ZmbGluZV9hY2Nlc3MiXSwiYW1yIjpbImV4dGVybmFsIl0sImNsaWVudF9pZCI6Ijk4N2NjOTcxLWZjMjItNDQ1NC05OWY5LTE2YzA3OGZhN2ZmNiIsInN1YiI6ImRmMjQ1MTlmLTVjYjMtNDBkOC1hM2JhLTExZDJkN2FhNGVlYSIsImF1dGhfdGltZSI6MTczODY4NjgyNCwiaWRwIjoiR29vZ2xlIiwidGVuYW50X2lkIjoiOTk0OTYyYTktNjcxZC00NGVkLTliZDMtNDBjNDJiZGIxMjRkIiwidGVuYW50aWQiOiI5OTQ5NjJhOS02NzFkLTQ0ZWQtOWJkMy00MGM0MmJkYjEyNGQiLCJzdWJkb21haW4iOiJmeW5kLmtla2EuY29tIiwidXNlcl9pZCI6IjFkYzJmNGYyLTkzNjUtNDk1Zi1iMDBhLTJhM2ViMjkxYWIyNiIsInVzZXJfaWRlbnRpZmllciI6IjFkYzJmNGYyLTkzNjUtNDk1Zi1iMDBhLTJhM2ViMjkxYWIyNiIsInVzZXJuYW1lIjoibW9oYW5wcmFzYWRAZ29meW5kLmNvbSIsImVtYWlsIjoibW9oYW5wcmFzYWRAZ29meW5kLmNvbSIsImF1dGhlbnRpY2F0aW9uX3R5cGUiOiIzIiwic2lkIjoiOEUwQzFBQjhCMUYwRDFFODBFODg2MjY0M0YzQUJCNkMiLCJqdGkiOiJDM0JGNUNFOEU2QTE2NkY4Q0Q1NjQyQ0Y5OUMxRTA0RSJ9.KAJIJQYkgkmQ4rVBoFYolzFEzfV3jTrTAxy3-WXGBTMa7pUAbt9ZVAHuXOi2oFg2EqdC5Iu9--QfkoUbHDFih2lZsMeh5THY3taNyFSSzxIl-H05WrfuQusXSLBGFOSvPb_-GTDvEUIB23dOKPq7iudwjxSokSIZPPV9Z6TZBLQtN6tnZr3b_WzcqyzkaDl1KXhz9kr_Y6-LzhOm5RapF1_ME39Tc4GQKNPSU74O1E-b0Ut0c62SKH3P2NJCQE4jjMXKbwLKs3YOTPTRKJ7C6bg0iKVyadmty1hABBg--FUQ7_z_XsoRFxlR6gAKAA-LqeTZmOAjVxsOnUWl11ilmw',
    'cache-control': 'no-cache',
    'content-type': 'application/json; charset=utf-8',
    'referer': 'https://fynd.keka.com/',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

unique_ids = set()

# Make the GET requests
for i in "abcdefghijklmnopqrstuvwxyz":
    response = requests.get(url + i, headers=headers)

    # Check for a successful response
    if response.status_code == 200:
        data = response.json()
        for employee in data.get("data", {}).get("employees", []):
            emp_id = employee.get("id")
            if emp_id:
                unique_ids.add(emp_id)
    else:
        print(f"Failed with status code: {response.status_code}")
        print(response.text)  # Print the error message

today = date.today()
print("Today's date is:", today)

print(unique_ids)
print('Total Count -> ', len(unique_ids))

# Optional: write to file
# with open("ids.txt", "w") as f:
#     for uid in unique_ids:
#         f.write(f"{uid}\n")
#     f.write(f"\nDate: {today}\n")
