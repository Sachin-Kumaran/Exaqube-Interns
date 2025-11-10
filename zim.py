import requests

url = "https://apigw.zim.com/digitalSchedules/Lines/v1/ZEX?subscription-key=9d63cf020a4c4708a7b0ebfe39578300&dateFrom=2025-11-10&dateTo=2026-02-18"

payload = {}
headers = {
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
  'access-control-allow-origin': '*',
  'cache-control': 'no-cache',
  'culture': 'en-US',
  'expires': '0',
  'origin': 'https://www.zim.com',
  'pageid': '16438',
  'pragma': 'no-cache',
  'priority': 'u=1, i',
  'referer': 'https://www.zim.com/',
  'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
  'Cookie': 'ak_bmsc=6F587BC27674ACA0D1F288D7377DCC5D~000000000000000000000000000000~YAAQdbxWaMIeFTCaAQAAAWQobR3tPVucTRM0iMwg17KpAftAOCN0zUDSGOHmFUvCCFjqDw+df4fLmnsADEZoedrRBLzAjaVIZOdqFB7qBGf6Os73HYdPpGACCAFNXB+YV1r91gfQhSrncgPJ855u/OADa1ltWc/JxREGmlcmgDFF/eQ87bgFTQFvec8yfsE+uwTiSkrNn8lp+6zV5UU9NOaYWnyGPk4XtVEgHY2CHK5wvJjCs29RlKCN2QAJcBdv47M3mdiMddwcA7clshg92GGUdzYcjzN68AKVESz66nD8OWqq6TyFkQpZXvcWPjZ26/pdhbqsmd0hC9IoMKcW0EDGJXcPjL/Mww==; dtCookie=v_4_srv_3_sn_DD2C88595E2E08825ACCBFE3B5977E7B_perc_100000_ol_0_mul_1_app-3A27cd3e94658c92f4_1_rcs-3Acss_0'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
