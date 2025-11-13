from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import pandas as pd
import json
from io import StringIO

url = "https://www.pilship.com/digital-solutions/?tab=customer&id=occ&label=pointToPoint&origin-port-code=JPTYO&destination-port-code=INMAA&start-date=2025-10-01&end-date=2025-11-29"

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Cookie": "_ga=GA1.1.991735325.1762765547; _ga_M39J8YZNDE=GS2.1.s1763009634$o3$g1$t1763010318$j59$l0$h0; OClmoOot=Ay4HBG2aAQAADDJ4PR8NFTpAFlml8_Hfi4MGCxYjGnuQxXEgHUCxJp9hcrrhAQ5g7U76K-mbwH9eCOfvosJeCA|1|0|dc45a1d1ad4b7674677a923aff48ed658a540806; wp-wpml_current_language=en; CookieConsent={stamp:'DtM1GmBGpvW6cjSVe2jU0rn9WnfW4Gz5tNWvwT4046+EL8vZvlTwyA==',necessary:true,preferences:true,statistics:true,marketing:true,method:'explicit',ver:1,utc:1762765544473,region:'in'}",
    "Priority": "u=3, i",
    "Referer": "https://www.pilship.com/digital-solutions/?tab=customer&id=schedules&label=pointToPoint&origin-port-code=JPTYO&destination-port-code=INMAA&start-date=2025-10-01&end-date=2025-11-29",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.1 Safari/605.1.15",
    "X-Requested-With": "XMLHttpRequest"
}

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    api = {"url": None}


    def on_request(request):
        if "schedules-point2point.php" in request.url:
            api["url"] = request.url


    page.on("request", on_request)
    page.goto(
        url,
        wait_until="domcontentloaded",
    )
    page.wait_for_timeout(10000)
    response = page.request.get(str(api["url"]), headers=headers)
    data = json.loads(response.text())
    browser.close()

html_content = data.get("schedulePointToPoint", {}).get("main", "")
soup = BeautifulSoup(html_content, "html.parser")
table = soup.find("table")

if table:
    df = pd.read_html(StringIO(str(table)))[0]
    df = df.loc[:, ~df.columns.str.contains("^Unnamed")]
    if "Port of Load" in df.columns:
        df = df.dropna(subset=["Port of Load"])
    df.to_csv("table_p2p.csv", index=False, encoding="utf-8-sig")
    print("Cleaned table saved as 'table_p2p.csv'")
else:
    print("No table found in the JSON 'main' field.")
