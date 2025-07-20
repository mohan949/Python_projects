import requests

url = "https://fynd.keka.com/k/default/api/employee/lookup/globalsearch?searchKey=a&includeRelivedEmployees=false"

payload = {}
headers = {
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjFBRjQzNjk5RUE0NDlDNkNCRUU3NDZFMjhDODM5NUIyMEE0MUNFMTgiLCJ4NXQiOiJHdlEybWVwRW5HeS01MGJpaklPVnNncEJ6aGciLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FwcC5rZWthLmNvbSIsIm5iZiI6MTcyNTUxNzk3OSwiaWF0IjoxNzI1NTE3OTc5LCJleHAiOjE3MjU2MDQzNzksImF1ZCI6WyJrZWthaHIuYXBpIiwiaGlyby5hcGkiLCJodHRwczovL2FwcC5rZWthLmNvbS9yZXNvdXJjZXMiXSwic2NvcGUiOlsib3BlbmlkIiwia2VrYWhyLmFwaSIsImhpcm8uYXBpIiwib2ZmbGluZV9hY2Nlc3MiXSwiYW1yIjpbImV4dGVybmFsIl0sImNsaWVudF9pZCI6Ijk4N2NjOTcxLWZjMjItNDQ1NC05OWY5LTE2YzA3OGZhN2ZmNiIsInN1YiI6ImRmMjQ1MTlmLTVjYjMtNDBkOC1hM2JhLTExZDJkN2FhNGVlYSIsImF1dGhfdGltZSI6MTY5MTU3MzkyNSwiaWRwIjoiR29vZ2xlIiwidGVuYW50X2lkIjoiOTk0OTYyYTktNjcxZC00NGVkLTliZDMtNDBjNDJiZGIxMjRkIiwidGVuYW50aWQiOiI5OTQ5NjJhOS02NzFkLTQ0ZWQtOWJkMy00MGM0MmJkYjEyNGQiLCJzdWJkb21haW4iOiJmeW5kLmtla2EuY29tIiwidXNlcl9pZCI6IjFkYzJmNGYyLTkzNjUtNDk1Zi1iMDBhLTJhM2ViMjkxYWIyNiIsInVzZXJfaWRlbnRpZmllciI6IjFkYzJmNGYyLTkzNjUtNDk1Zi1iMDBhLTJhM2ViMjkxYWIyNiIsInVzZXJuYW1lIjoibW9oYW5wcmFzYWRAZ29meW5kLmNvbSIsImVtYWlsIjoibW9oYW5wcmFzYWRAZ29meW5kLmNvbSIsImF1dGhlbnRpY2F0aW9uX3R5cGUiOiIzIiwic2lkIjoiNEExMzNFRkE3RDI0M0IzNkFDNEY5MUEzNzdENzk1NzUiLCJqdGkiOiIwMTEyMUU1MkVCQkQ5N0VCRTQ2RDc5NEQwRDVFQTI2QiJ9.FBsUCvn6_k8-l-0ay15SPsi0sG1-kD1ANe70Owtwk_gdD1Dk1nH8h9bYbuI-MRyb0M9y8QU-ByawXGR8TGY4OH2PwCl7S54-P4ACX9ZxKlOdQtrIY76Il3CxCKmsYjL-H1f7HLkPCIjEXj304XpfBkSdrpgcarxwAzD9ybiuu1VC8NnmM-0X6C9g3HCzP0U5lpnm1u9ajo0skE9_Y3eVt29EEftqAL1Bp7IFHfXEcCDmPwxOpJxYNSIrKIxcjKJJ1IyFApytZh2MLTmwjUJIQDhrocjkaG96dcCC5sh3nhs7LG6yhPHGYhl31UAI78B_xduIxRy29en8YX40IGsESQ',
  'cache-control': 'no-cache',
  'content-type': 'application/json; charset=utf-8',
  'cookie': '_ga=GA1.1.1438795970.1715788379; Subdomain=fynd.keka.com; ai_user=UL/DIiivu5t+JWXa4G1uJa|2024-05-15T15:53:05.110Z; .AspNetCore.Session=CfDJ8PDzqe7kd4tNu305VbGcogYPn7j3hg%2BdZMcmssZWVEKxDJDaKo7ieExxDHgXUoF9EemhUzZ1OPNb7nwax3bpsqyAxUZ%2BbOBeEnsE4p2rGu98Ee4zqCTt2RLRh0ygJs2hGphSq1%2FZpDdwVbXv3NoBqRfsL1J%2BB1OcQ53WyDbywyV5; messagesUtk=a04d18921c34487aab5de134f9991d5f; _ga_RFKWJDYLYV=GS1.1.1720594160.44.0.1720594163.0.0.0; _ga_19064LH1ZY=GS1.1.1720594161.44.0.1720594163.58.0.0; _clck=1v7xm9y%7C2%7Cfop%7C0%7C1701; hubspotutk=f06e08512a895ad82b72cc0ef8f98bb3; __hssrc=1; _gcl_au=1.1.1375643642.1724843935; _ga_LVR3B71RG5=GS1.1.1724849327.46.0.1724849327.60.0.0; _fbp=fb.1.1724849327815.256010607691342337; _uetvid=d1e4aea06f1611eea19ba310b4f378dc; __hstc=118268374.f06e08512a895ad82b72cc0ef8f98bb3.1724843933774.1724843933774.1724849329205.2; geo=IN; usergeocode=IN; ai_session=aU8PCos5m9TuadA1pH2xfh|1725552985901|1725553153426; _dd_s=logs=1&id=e0395931-b767-4879-97b5-a8832bd2d09d&created=1725552984361&expire=1725554138270',
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

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
