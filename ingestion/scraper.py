import requests
import re
from bs4 import BeautifulSoup

url = "https://example.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)

def clean_funding(text):
    numbers = re.sub(r'[^0-9]', '', text)

    if numbers:
        return int(numbers)

    return 0

print(clean_funding("$2,500,000"))