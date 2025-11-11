import requests

url = "https://www.summitshipping.sg/img/containers/assets/images/pages/yds-service-1760974616.png/b7a3c7a8431fa4b6301d3015ea6eb4ae.png"

payload = {}
headers = {
  'sec-ch-ua-platform': '"Windows"',
  'Referer': 'https://www.summitshipping.sg/schedule',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'Cookie': 'XSRF-TOKEN=eyJpdiI6ImNKcUxnZlNHTDJFMWZ3TW1UbUFRYWc9PSIsInZhbHVlIjoiek1cLzNqUW5xQitnZXdGd1lrQ0N6MEN6dys4WU1VbUJqd2lWNHBTS0ZSNmZPYlFYQ0JyQ1NZRjJ0d1J2T3U2ZVJlcm8raXhIN0lGR0lJanI2UmhOaTh3PT0iLCJtYWMiOiI1NTVmMDU3OGI3NzExMDM4NDg2MzczZjM5ZjhmZjhiNWNhOWE5ODc5MTNjMDA4MWU5MjM3YjMzNGY3YTE3MzczIn0%3D; laravel_session=eyJpdiI6InhqRG0zOVpuVWtIZWt5WkRydmQ1Z0E9PSIsInZhbHVlIjoicEpSUFZ5NTBsdFBZWEpEUTlFdHlsWFVKT2ZyRXppTU5LVXVOclduQWxMWDIyR1B2aFVUcEZOVFVySkFiTnBvZmpuM2RFK2dyVU9pWm1SeXZyUDZsV0E9PSIsIm1hYyI6Ijk2NDc1ODM1MGNkNjM4ZTQyZWJlNTdhOGExMjYwOTlhYTliN2QyZTVkMTc4NmMxMjY5NTJiMWQ0NjgxMzQ1NzQifQ%3D%3D'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
