import requests
from PIL import Image
import pytesseract
from io import BytesIO
import json

# 👇 Add the path to your Tesseract installation
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Image URL from Summit Shipping
image_url = "https://www.summitshipping.sg/img/containers/assets/images/pages/yds-service-1760974616.png/b7a3c7a8431fa4b6301d3015ea6eb4ae.png"

# Optional headers
headers = {
    "Referer": "https://www.summitshipping.sg/schedule",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
}

# Download the image
response = requests.get(image_url, headers=headers)
img = Image.open(BytesIO(response.content))

# Extract text using Tesseract OCR
text = pytesseract.image_to_string(img)

# Show extracted text
print("Extracted Text:\n", text)

# Save text to a JSON file
data = {"image_url": image_url, "extracted_text": text.strip()}
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("\n✅ Text successfully saved to output.json")
