import requests
from datetime import date


# URL
url = 'https://fynd.keka.com/k/default/api/employee/lookup/globalsearch?searchKey='

# Headers
headers = {
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjFBRjQzNjk5RUE0NDlDNkNCRUU3NDZFMjhDODM5NUIyMEE0MUNFMTgiLCJ4NXQiOiJHdlEybWVwRW5HeS01MGJpaklPVnNncEJ6aGciLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FwcC5rZWthLmNvbSIsIm5iZiI6MTczNDg3Nzc0MCwiaWF0IjoxNzM0ODc3NzQwLCJleHAiOjE3MzQ5NjQxNDAsImF1ZCI6WyJrZWthaHIuYXBpIiwiaGlyby5hcGkiLCJodHRwczovL2FwcC5rZWthLmNvbS9yZXNvdXJjZXMiXSwic2NvcGUiOlsib3BlbmlkIiwia2VrYWhyLmFwaSIsImhpcm8uYXBpIiwib2ZmbGluZV9hY2Nlc3MiXSwiYW1yIjpbImV4dGVybmFsIl0sImNsaWVudF9pZCI6Ijk4N2NjOTcxLWZjMjItNDQ1NC05OWY5LTE2YzA3OGZhN2ZmNiIsInN1YiI6ImRmMjQ1MTlmLTVjYjMtNDBkOC1hM2JhLTExZDJkN2FhNGVlYSIsImF1dGhfdGltZSI6MTY5MTU3MzkyNSwiaWRwIjoiR29vZ2xlIiwidGVuYW50X2lkIjoiOTk0OTYyYTktNjcxZC00NGVkLTliZDMtNDBjNDJiZGIxMjRkIiwidGVuYW50aWQiOiI5OTQ5NjJhOS02NzFkLTQ0ZWQtOWJkMy00MGM0MmJkYjEyNGQiLCJzdWJkb21haW4iOiJmeW5kLmtla2EuY29tIiwidXNlcl9pZCI6IjFkYzJmNGYyLTkzNjUtNDk1Zi1iMDBhLTJhM2ViMjkxYWIyNiIsInVzZXJfaWRlbnRpZmllciI6IjFkYzJmNGYyLTkzNjUtNDk1Zi1iMDBhLTJhM2ViMjkxYWIyNiIsInVzZXJuYW1lIjoibW9oYW5wcmFzYWRAZ29meW5kLmNvbSIsImVtYWlsIjoibW9oYW5wcmFzYWRAZ29meW5kLmNvbSIsImF1dGhlbnRpY2F0aW9uX3R5cGUiOiIzIiwic2lkIjoiNEExMzNFRkE3RDI0M0IzNkFDNEY5MUEzNzdENzk1NzUiLCJqdGkiOiI0OEM5NDI0Q0VENkNCNkI4NDQ4MTNDRDBDRkYwRTVDMSJ9.DCRyiP1wML2vrsCkO30VBVmg-U5ZIhK1I9JKnOrk8Fk5WiFnNsTVx3hTuRtNmyt4exqIvKXMIOxRyFqA9NGjUwIB-EYAKAYFKHbtSKFEgEeBvY_ngJksrxbsh-a-Fbu88t0bJ7dH40PtoNs7MZYV-gVPaECc02uXqvrYaOLWwyOEfWoc9vpCNeZtbGJ0IwouC4ifDXmI4hJjAG95nM0hB0JyD7Fplbb4425p6hbTokEeNGdK2UOcYBDVXeL8NMj6gAz5fcUpaHp0gGY1goMk3xjSYLPz4zrzEq_gHtOmgX432JNbsHczrvruGa7gO0xhHMoZeSCVkatLVukJXBpPgQ',
  'cache-control': 'no-cache',
  'content-type': 'application/json; charset=utf-8',
  'cookie': '_ga=GA1.1.1438795970.1715788379; Subdomain=fynd.keka.com; ai_user=UL/DIiivu5t+JWXa4G1uJa|2024-05-15T15:53:05.110Z; .AspNetCore.Session=CfDJ8PDzqe7kd4tNu305VbGcogYPn7j3hg%2BdZMcmssZWVEKxDJDaKo7ieExxDHgXUoF9EemhUzZ1OPNb7nwax3bpsqyAxUZ%2BbOBeEnsE4p2rGu98Ee4zqCTt2RLRh0ygJs2hGphSq1%2FZpDdwVbXv3NoBqRfsL1J%2BB1OcQ53WyDbywyV5; messagesUtk=a04d18921c34487aab5de134f9991d5f; _ga_RFKWJDYLYV=GS1.1.1720594160.44.0.1720594163.0.0.0; _ga_19064LH1ZY=GS1.1.1720594161.44.0.1720594163.58.0.0; _clck=1v7xm9y%7C2%7Cfop%7C0%7C1701; hubspotutk=f06e08512a895ad82b72cc0ef8f98bb3; __hssrc=1; _ga_LVR3B71RG5=GS1.1.1724849327.46.0.1724849327.60.0.0; _uetvid=d1e4aea06f1611eea19ba310b4f378dc; __hstc=118268374.f06e08512a895ad82b72cc0ef8f98bb3.1724843933774.1724843933774.1724849329205.2; geo=IN; ai_session=nvLcNIJE97hQ4CFA6LpSwD|1732719729364|1732719739246; _dd_s=logs=1&id=4b12e086-2529-44ae-8de5-07e27b3fbc7f&created=1732719727264&expire=1732720756503',
  'pragma': 'no-cache',
  'priority': 'u=1, i',
  'referer': 'https://fynd.keka.com/',
  'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
  'x-requested-with': 'XMLHttpRequest'
}

# bearer = input("Please enter bearer Token")
# headers["authorization"] = bearer


res = set()
# Make the GET request
for i in "abcdefghijklmnopqrstuvwxyz":
    response = requests.get(url+i, headers=headers)

    # Check for a successful response
    if response.status_code == 200:
        data = response.json()
        for employee in data.get("data", {}).get("employees", []):
            if employee.get("exitStatus") == 1:
                res.add(employee.get("displayName"))
    else:
        print(f"Failed with status code: {response.status_code}")
        print(response.text)  # Print the error message

today = date.today()
print("Today's date is:", today)

print(res)
print('Total Count -> ',len(res))

# res_string = ', '.join(res)
# f = open("sushant.txt","w")
# f.write(res_string)
# f = open("sushant.txt","a")
# f.write(today)
# f.close()