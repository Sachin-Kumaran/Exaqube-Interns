import requests

line_code = "ZMP"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
}

response=requests.get(f"https://apigw.zim.com/digitalSchedules/Lines/v1/{line_code}?subscription-key=9d63cf020a4c4708a7b0ebfe39578300&dateFrom=2025-11-13&dateTo=2026-02-21", headers=headers)
print(response.text)
