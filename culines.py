import requests

url = "https://www.culines.com/search/getDataBase"

payload = "trade=WAT&lane=IMR"
headers = {
  'accept': 'application/json, text/javascript, */*; q=0.01',
  'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'origin': 'https://www.culines.com',
  'priority': 'u=1, i',
  'referer': 'https://www.culines.com/en/site/route',
  'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
  'x-requested-with': 'XMLHttpRequest',
  'Cookie': 'PHPSESSID=4g8c9k28jdmvjdq4rbs3hslmv0; Hm_lvt_9dc5e71f248278ef6619490e5d46398b=1762758021; HMACCOUNT=4A6500661A68410F; Hm_lpvt_9dc5e71f248278ef6619490e5d46398b=1762758123'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
