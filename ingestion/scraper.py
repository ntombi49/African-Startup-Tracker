import requests
import re
from bs4 import BeautifulSoup
import psycopg2

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

startup = {
    "company_name": "Paystack",
    "country": "Nigeria",
    "sector": "FinTech",
    "funding": 200000000
}

print(startup)

conn = psycopg2.connect(
    host="localhost",
    database="startup_db",
    user="postgres",
    password="LizzyMkansi@123"
)