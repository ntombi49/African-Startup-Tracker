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

# database connection
conn = psycopg2.connect(
    host="localhost",
    database="startup_db",
    user="postgres",
    password="LizzyMkansi@123"
)

cursor = conn.cursor() 

# inserted Test Data
cursor.execute(
    """
    INSERT INTO startups
    (
        company_name,
        origin_country,
        target_sector,
        funding_amount,
        source_url
    )
    VALUES (%s,%s,%s,%s,%s)
    """,
    (
        "Paystack",
        "Nigeria",
        "FinTech",
        200000000,
        "https://example.com"
    )
)

conn.commit()  #save changes
cursor.close()  #Close connection
conn.close()