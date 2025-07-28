import requests
import time
import csv
import os
from datetime import datetime


def send_slack_notification(message, webhook_url):
    import requests
    payload = {"text": message}
    resp = requests.post(webhook_url, json=payload)
    if resp.status_code == 200:
        print("✅ Slack notification sent to Slack.")
    else:
        print(f"❌ Slack notification failed: {resp.status_code} - {resp.text}")


def send_detailed_slack_report(results, csv_file, env_name, webhook_url):
    import requests

    # Build Slack message lines with headers
    header = (
        f"*GTmetrix Report - {env_name}*\n"
        f"Results saved to `{csv_file}`\n"
        "-------------------------------------------------\n"
        "*Date* | *Page Name* | *Perf Score* | *Onload (ms)* | *Fully Loaded (ms)* | *Page Size* | *Requests* | *Report URL* | *Error*\n"
    )
    lines = [header]

    for row in results:
        (date, url, env, page_name, perf, onload, loaded, size, reqs, report_url, error) = row
        lines.append(
            f"{date} | {page_name} | {perf or '-'} | {onload or '-'} | {loaded or '-'} | {size or '-'} | {reqs or '-'} | <{report_url or url}|Report> | {error or '-'}"
        )

    msg = "\n".join(lines)
    payload = {"text": msg}
    resp = requests.post(webhook_url, json=payload)
    if resp.status_code == 200:
        print("✅ Detailed Slack notification sent.")
    else:
        print(f"❌ Slack notification failed: {resp.status_code} - {resp.text}")



test_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

os.environ['REQUESTS_CA_BUNDLE'] = '/etc/ssl/cert.pem'

# GTmetrix API credentials and endpoint
API_KEY = "59516b35bf1cfe8713bf675737d8a472"
BASE_URL = "https://gtmetrix.com/api/2.0/"

# ---- UAT and PROD hardcoded URLs and Page Names ----
uat_urls = [
    ("https://hugo-boss-uat.fynd.io/", "Home"),
    # ("https://hugo-boss-uat.fynd.io/sections/hugo-home", "Home-Hugo"),
    # ("https://hugo-boss-uat.fynd.io/sections/boss-home", "Home-Boss"),
    # ("https://hugo-boss-uat.fynd.io/product/cotton-terry-tracksuit-bottoms-with-red-logo-label-13475192-14551104", "PDP"),
    # ("https://hugo-boss-uat.fynd.io/collection/sale-men-t-shirts", "PLP"),
    # ("https://hugo-boss-uat.fynd.io/products/?q=shoes", "PLP-Search"),
]
prod_urls = [
    ("https://hugoboss.ae/", "Home"),
    ("https://hugoboss.ae/sections/boss-home", "Home-Boss"),
    ("https://hugoboss.ae/sections/hugo-home", "Home-Hugo"),
    ("https://hugoboss.ae/product/two-pack-of-cotton-blend-regular-length-socks-13516296", "PDP"),
    ("https://hugoboss.ae/collection/men-all-new-arrivals?brand=hugo", "PLP-Hugo"),
    ("https://hugoboss.ae/products/?q=shoes", "PLP-Search"),
]

# ----- Environment selection -----
env_choice = input("Select environment to test (UAT/PROD): ").strip().lower()
if env_choice == "uat":
    env_name = "UAT"
    urls_to_test = uat_urls
elif env_choice == "prod":
    env_name = "PROD"
    urls_to_test = prod_urls
else:
    print("Invalid environment selection. Please choose 'UAT' or 'PROD'.")
    exit(1)

headers = {
    "Content-Type": "application/vnd.api+json",
    "Accept": "application/vnd.api+json"
}

results = []
for url, page_name in urls_to_test:
    print(f"\n=== Testing: {url} ({page_name}) ===")

    payload = {
        "data": {
            "type": "test",
            "attributes": {
                "url": url
            }
        }
    }

    try:
        response = requests.post(BASE_URL + "tests", headers=headers, json=payload,
                                 auth=(API_KEY, ""))
    except Exception as e:
        print(f"Error: Failed to send request to GTmetrix API - {e}")
        results.append([url, env_name, page_name, "", "", "", "", "", f"Exception: {e}"])
        continue

    if response.status_code != 202:
        try:
            error_info = response.json()
        except ValueError:
            error_info = None
        if error_info and "errors" in error_info:
            err = error_info["errors"][0]
            err_msg = f"{err.get('title')}: {err.get('detail')}"
        else:
            err_msg = response.text
        print(f"Failed to start test: HTTP {response.status_code} - {err_msg}")
        results.append([url, env_name, page_name, "", "", "", "", "", f"Failed to start: {err_msg}"])
        continue

    test_data = response.json().get("data", {})
    test_id = test_data.get("id")
    if not test_id:
        print("Failed to retrieve test ID from response.")
        results.append([url, env_name, page_name, "", "", "", "", "", "No test ID"])
        continue

    print(f"Test started (ID: {test_id}). Polling for completion...")

    test_status_url = BASE_URL + f"tests/{test_id}"
    report_url = None
    max_polls = 40
    poll_count = 0

    while poll_count < max_polls:
        poll_count += 1
        try:
            status_resp = requests.get(test_status_url, headers=headers, auth=(API_KEY, ""), allow_redirects=False)
        except Exception as e:
            print(f"Error: Failed to poll test status - {e}")
            results.append([url, env_name, page_name, "", "", "", "", "", f"Polling exception: {e}"])
            break
        
        if status_resp.status_code == 303:
            report_url = status_resp.headers.get("Location")
            if report_url and report_url.startswith("/"):
                report_url = "https://gtmetrix.com" + report_url
            print("Test completed. Report URL obtained from redirect.")
            break

        if status_resp.status_code == 200:
            status_json = status_resp.json()
            data = status_json.get("data", {})
            attributes = data.get("attributes", {})
            state = attributes.get("state")
            if state == "completed":
                report_id = attributes.get("report")
                if report_id:
                    report_url = BASE_URL + f"reports/{report_id}"
                    print("Test completed. Report ID obtained from status payload.")
                    break
                else:
                    print("Test completed but report ID missing in response.")
                    results.append([url, env_name, page_name, "", "", "", "", "", "No report ID"])
                    break
            elif state == "error":
                error_msg = attributes.get("error", "Unknown error")
                print(f"Test failed (state=error): {error_msg}")
                results.append([url, env_name, page_name, "", "", "", "", "", f"Error: {error_msg}"])
                break
            else:
                time.sleep(3)
                continue
        else:
            if status_resp.status_code == 404:
                print("Error: Test not found (received 404). It may have expired or the ID is incorrect.")
                results.append([url, env_name, page_name, "", "", "", "", "", "Test not found (404)"])
            elif status_resp.status_code == 429:
                print("Error: Rate limit exceeded or too many concurrent requests (429).")
                results.append([url, env_name, page_name, "", "", "", "", "", "Rate limit/concurrency error (429)"])
            else:
                print(f"Unexpected response: HTTP {status_resp.status_code} - {status_resp.text}")
                results.append([url, env_name, page_name, "", "", "", "", "", f"Unexpected response: {status_resp.status_code}"])
            break
    else:
        print("Error: Test did not complete within expected time.")
        results.append([url, env_name, page_name, "", "", "", "", "", "Timeout"])
        continue

    if not report_url:
        print("Error: Report URL could not be determined.")
        results.append([url, env_name, page_name, "", "", "", "", "", "No report URL"])
        continue

    try:
        report_resp = requests.get(report_url, headers=headers, auth=(API_KEY, ""))
    except Exception as e:
        print(f"Error: Failed to retrieve report data - {e}")
        results.append([url, env_name, page_name, "", "", "", "", "", f"Report exception: {e}"])
        continue

    if report_resp.status_code != 200:
        print(f"Failed to get report: HTTP {report_resp.status_code} - {report_resp.text}")
        results.append([url, env_name, page_name, "", "", "", "", "", f"Failed to get report: {report_resp.status_code}"])
        continue

    report_json = report_resp.json()
    report_data = report_json.get("data", {})
    report_attrs = report_data.get("attributes", {})
    report_links = report_data.get("links", {}) 

    perf_score     = report_attrs.get("performance_score")
    onload_time    = report_attrs.get("onload_time")
    fully_loaded   = report_attrs.get("fully_loaded_time")
    page_bytes     = report_attrs.get("page_bytes")
    page_requests  = report_attrs.get("page_requests")
   # report_url_val = report_attrs.get("report_url")
    report_url_val = report_links.get("report_url")

    print(f"Tested URL: {url}")
    print(f"Performance Score: {perf_score}")
    print(f"Load Time (onload): {onload_time} ms")
    print(f"Fully Loaded Time: {fully_loaded} ms")
    print(f"Total Page Size: {page_bytes} bytes")
    print(f"Total Requests: {page_requests}")
    print(f"Report URL: {report_url_val}")

    results.append([
         test_date, url, env_name, page_name, perf_score, onload_time, fully_loaded, page_bytes, page_requests,report_url_val, ""
    ])

# Save all results to CSV
csv_file = "gtmetrix_report.csv"
try:
    with open(csv_file, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Date","URL", "Env", "Page Name", "Performance Score",
            "Onload Time (ms)", "Fully Loaded Time (ms)",
            "Total Page Size (bytes)", "Total Requests", "Report URL", "Error"
        ])
        writer.writerows(results)
    print(f"\nResults saved to {csv_file}")
except Exception as e:
    print(f"Error writing CSV file: {e}")

# SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"  # <--- replace with your webhook

# summary = f"GTmetrix batch for {env_name} completed.\n"
# summary += f"CSV: {csv_file}\n"
# success_count = sum(1 for row in results if not row[-1])
# fail_count = sum(1 for row in results if row[-1])
# summary += f"✅ Passed: {success_count}, ❌ Failed: {fail_count}"
# if results:
#     summary += f"\nFirst tested page: {results[0][1]} ({results[0][3]})"

# send_slack_notification(summary, SLACK_WEBHOOK_URL)

SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"  # <-- your webhook URL

send_detailed_slack_report(results, csv_file, env_name, SLACK_WEBHOOK_URL)
