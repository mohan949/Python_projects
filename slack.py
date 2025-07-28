import requests

SLACK_WEBHOOK_URL = 'https://hooks.slack.com/services/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'

message = "✅ This is a test notification from Python script to your Slack channel!"

payload = {
    "text": message
}

response = requests.post(SLACK_WEBHOOK_URL, json=payload)

if response.status_code == 200:
    print("Slack notification sent successfully!")
else:
    print(f"Failed to send notification: {response.status_code} - {response.text}")
