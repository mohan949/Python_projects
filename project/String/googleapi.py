# import requests
# import json

# url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=23.022519,72.566983&key=AIzaSyAVCJQAKy6UfgFqZUNABAuGQp2BkGLhAgI"

# payload = {}
# headers = {
#   'Content-Type': 'application/json',
#   'account-token': 'ebe5a392-40eb-4f64-8eec-1fb739d1f94c'
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)

import requests
import json

# Take user input for latitude and longitude
latitude = input("Enter latitude: ")
longitude = input("Enter longitude: ")

# Construct the URL dynamically
api_key = "AIzaSyAVCJQAKy6UfgFqZUNABAuGQp2BkGLhAgI"  # Replace with your actual API key
url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={api_key}"

# Set up headers
headers = {
    'Content-Type': 'application/json',
    'account-token': 'ebe5a392-40eb-4f64-8eec-1fb739d1f94c'  # If required by your service
}

# Make the request
response = requests.get(url, headers=headers)

# Print response
print(response.json())  # Pretty print JSON response
