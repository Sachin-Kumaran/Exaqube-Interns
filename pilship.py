import requests

url = "https://www.pilship.com/wp-content/themes/hello-theme-child-master/pil-api/schedules-byport.php?port_code=INMAA&selected_portname=%5BINMAA%5D%20CHENNAI&byport_selectedstartdate=2025-11-10&byport_selectedenddate=2025-11-29&n=1762765203%7C6248f694b6e90a8e3dddcfe905c7bf41&timestamp=1762765717881"

payload = {}
headers = {
  'Accept': '*/*',
  'Sec-Fetch-Site': 'same-origin',
  'Accept-Language': 'en-US,en;q=0.9',
  'Accept-Encoding': 'gzip, deflate, br',
  'Sec-Fetch-Mode': 'cors',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0.1 Safari/605.1.15',
  'Referer': 'https://www.pilship.com/digital-solutions/?tab=customer&id=schedules&label=byPort&port-code=INMAA&start-date=2025-11-10&end-date=2025-11-29',
  'Connection': 'keep-alive',
  'Cookie': '_ga_M39J8YZNDE=GS2.1.s1762765546$o1$g1$t1762765723$j23$l0$h0; _ga=GA1.1.991735325.1762765547; OClmoOot=Ay4HBG2aAQAADDJ4PR8NFTpAFlml8_Hfi4MGCxYjGnuQxXEgHUCxJp9hcrrhAQ5g7U76K-mbwH9eCOfvosJeCA|1|0|dc45a1d1ad4b7674677a923aff48ed658a540806; wp-wpml_current_language=en; CookieConsent={stamp:%27DtM1GmBGpvW6cjSVe2jU0rn9WnfW4Gz5tNWvwT4046+EL8vZvlTwyA==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1762765544473%2Cregion:%27in%27}',
  'Sec-Fetch-Dest': 'empty',
  'X-Requested-With': 'XMLHttpRequest',
  'Priority': 'u=3, i'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
