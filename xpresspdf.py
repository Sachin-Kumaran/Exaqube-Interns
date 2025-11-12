import requests
from bs4 import BeautifulSoup

base_url = "https://www.x-pressfeeders.com/services-and-schedules"
url=base_url+"-details?code=ADX+1&id=66719588371&pol=&pod=&r=1762948048534"

response = requests.get(url)
response.raise_for_status()  # Stop if the request fails
  
soup = BeautifulSoup(response.text, "html.parser")

pdf_container = soup.find("div", {"id": "pdfContainer"})

if pdf_container:
    # Find the <object> tag inside that div
    obj_tag = pdf_container.find("object")
    if obj_tag and obj_tag.has_attr("data"):
        pdf_url = obj_tag["data"]
        print("PDF URL found:", pdf_url)
    else:
        print("No <object> tag or 'data' attribute found inside #pdfContainer.")
else:
    print("No div found with id='pdfContainer'.")
