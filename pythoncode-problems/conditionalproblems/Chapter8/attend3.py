import requests

url = "https://fynd.keka.com/k/default/api/employee/lookup/globalsearch?searchKey=a&includeRelivedEmployees=false"

payload = {}
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjFBRjQzNjk5RUE0NDlDNkNCRUU3NDZFMjhDODM5NUIyMEE0MUNFMTgiLCJ4NXQiOiJHdlEybWVwRW5HeS01MGJpaklPVnNncEJ6aGciLCJ0eXAiOiJKV1QifQ',
    'cache-control': 'no-cache',
    'content-type': 'application/json; charset=utf-8',
    'cookie': '_ga=GA1.1.1438795970.1715788379; Subdomain=fynd.keka.com;',
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

# Send the request
response = requests.get(url, headers=headers, data=payload)

# Parse response to JSON
try:
    data = response.json()  # Ensure the response is parsed as JSON
except ValueError:
    print("Error: Response is not a valid JSON.")
    data = None

# Access the 'employees' list inside the response
if data and isinstance(data, dict) and "data" in data and "employees" in data["data"]:
    employees = data["data"]["employees"]["exitStatus"]

    # Filter items with exitStatus == 1
    filtered_items = [item for item in employees if item.get('exitStatus') == 1]

    # Count the number of such items
    exit_status_count = len(filtered_items)

    # Print the result
    print(f"Number of employees with exitStatus = 1: {exit_status_count}")
else:
    print("Error: Expected a dictionary with 'data' and 'employees' keys.")
