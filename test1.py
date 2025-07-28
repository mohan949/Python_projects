import requests
import os
from requests.auth import HTTPBasicAuth

# Fix SSL certificate verification issue on macOS
os.environ['REQUESTS_CA_BUNDLE'] = '/etc/ssl/cert.pem'

api_key = '59516b35bf1cfe8713bf675737d8a472'

# Correct: API key as username, empty password
response = requests.get(
    'https://gtmetrix.com/api/2.0/status',
    auth=HTTPBasicAuth(api_key, '')  # ✅ This is correct
)

print(response.status_code)
print(response.json())
