import requests
from datetime import date


# URL
url = 'https://fynd.keka.com/k/default/api/employee/lookup/globalsearch?searchKey='

# Headers
headers = {
    'accept': 'application/json, text/plain, /',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjFBRjQzNjk5RUE0NDlDNkNCRUU3NDZFMjhDODM5NUIyMEE0MUNFMTgiLCJ4NXQiOiJHdlEybWVwRW5HeS01MGJpaklPVnNncEJ6aGciLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FwcC5rZWthLmNvbSIsIm5iZiI6MTcyOTY5MzI3MCwiaWF0IjoxNzI5NjkzMjcwLCJleHAiOjE3Mjk3Nzk2NzAsImF1ZCI6WyJrZWthaHIuYXBpIiwiaGlyby5hcGkiLCJodHRwczovL2FwcC5rZWthLmNvbS9yZXNvdXJjZXMiXSwic2NvcGUiOlsib3BlbmlkIiwia2VrYWhyLmFwaSIsImhpcm8uYXBpIiwib2ZmbGluZV9hY2Nlc3MiXSwiYW1yIjpbImV4dGVybmFsIl0sImNsaWVudF9pZCI6Ijk4N2NjOTcxLWZjMjItNDQ1NC05OWY5LTE2YzA3OGZhN2ZmNiIsInN1YiI6ImRmMjQ1MTlmLTVjYjMtNDBkOC1hM2JhLTExZDJkN2FhNGVlYSIsImF1dGhfdGltZSI6MTY5MTU3MzkyNSwiaWRwIjoiR29vZ2xlIiwidGVuYW50X2lkIjoiOTk0OTYyYTktNjcxZC00NGVkLTliZDMtNDBjNDJiZGIxMjRkIiwidGVuYW50aWQiOiI5OTQ5NjJhOS02NzFkLTQ0ZWQtOWJkMy00MGM0MmJkYjEyNGQiLCJzdWJkb21haW4iOiJmeW5kLmtla2EuY29tIiwidXNlcl9pZCI6IjFkYzJmNGYyLTkzNjUtNDk1Zi1iMDBhLTJhM2ViMjkxYWIyNiIsInVzZXJfaWRlbnRpZmllciI6IjFkYzJmNGYyLTkzNjUtNDk1Zi1iMDBhLTJhM2ViMjkxYWIyNiIsInVzZXJuYW1lIjoibW9oYW5wcmFzYWRAZ29meW5kLmNvbSIsImVtYWlsIjoibW9oYW5wcmFzYWRAZ29meW5kLmNvbSIsImF1dGhlbnRpY2F0aW9uX3R5cGUiOiIzIiwic2lkIjoiNEExMzNFRkE3RDI0M0IzNkFDNEY5MUEzNzdENzk1NzUiLCJqdGkiOiI4NUFCNDVCRjlFMzQ0RjVGM0QwOTk1RkRERUE5RkVEOCJ9.bXaSCpbVBfIW0tKkp_cRwhbqbSwmdORFJJ3asbeUm3d_QxbGMPlPLpcwAnQJg7H6Kcq690VJBL7ACbPPnUFIl0Ium2Qrey5oMMKQ5wprxPZJ_qg0662YrD8u6qfUxrfLNsHo6RFpmCRQFzJZQ4Qos9bpFPKECrPLSGGL1x_6_NwOxv9IMXmNem5VgY6gEsjDQsqGbeuXAOqfWvaHVdc_spiIO4n6zpousguyJv8uCmEGDMAHp18WmAC9ucb1WVkdqdHrAVHGTtuRmr2GH4h5mIevL3lW6HzyD_AP3NuM4SudO7Dx3D9VsghurtLgZSBOojjYWmLoAC9z05a9NfmJ-Q',
    'cache-control': 'no-cache',
    'content-type': 'application/json; charset=utf-8',
    'cookie': '_ga=GA1.1.1438795970.1715788379; Subdomain=fynd.keka.com; ai_user=UL/DIiivu5t+JWXa4G1uJa|2024-05-15T15:53:05.110Z; .AspNetCore.Session=CfDJ8PDzqe7kd4tNu305VbGcogYPn7j3hg%2BdZMcmssZWVEKxDJDaKo7ieExxDHgXUoF9EemhUzZ1OPNb7nwax3bpsqyAxUZ%2BbOBeEnsE4p2rGu98Ee4zqCTt2RLRh0ygJs2hGphSq1%2FZpDdwVbXv3NoBqRfsL1J%2BB1OcQ53WyDbywyV5; messagesUtk=a04d18921c34487aab5de134f9991d5f; _ga_RFKWJDYLYV=GS1.1.1720594160.44.0.1720594163.0.0.0; _ga_19064LH1ZY=GS1.1.1720594161.44.0.1720594163.58.0.0; _clck=1v7xm9y%7C2%7Cfop%7C0%7C1701; hubspotutk=f06e08512a895ad82b72cc0ef8f98bb3; __hssrc=1; _gcl_au=1.1.1375643642.1724843935; _ga_LVR3B71RG5=GS1.1.1724849327.46.0.1724849327.60.0.0; _fbp=fb.1.1724849327815.256010607691342337; _uetvid=d1e4aea06f1611eea19ba310b4f378dc; __hstc=118268374.f06e08512a895ad82b72cc0ef8f98bb3.1724843933774.1724843933774.1724849329205.2; geo=IN; usergeocode=IN; ai_session=unvdiefwb1r4/OuTnObQYa|1726765873659|1726765873659; _dd_s=logs=1&id=d6c04a56-1860-47c7-bd7a-f261575f3911&created=1726765870107&expire=1726766845203',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://fynd.keka.com/',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
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
print('--------------------------------------------------------------------------------------------------------')
print("Today's date is ->", today)
print('Total Count -> ',len(res))
print(res)
print('--------------------------------------------------------------------------------------------------------')



date_string = today.strftime('%Y-%m-%d ')
f = open("sushant.txt","w")
f.write(date_string) 

res_string = ', '.join(res)
f = open("sushant.txt","a")
f.write(res_string)

# line = f.writelines()
# while(line !=''):
#     line = f.writelines(res_string)
f.close()