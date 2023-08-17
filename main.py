#!/usr/bin/env python3

# import os
import requests
from bs4 import BeautifulSoup

# URL to fetch HTML content from
# url = os.getenv("product_url")
url = "https://www.newegg.ca/synology-ds1522/p/N82E16822108819"

# Fetch the HTML content
response = requests.get(url)
html_content = response.text

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find the price-current element within the ul with class price
price_element = soup.select_one("ul.price li.price-current strong")
if price_element:
    price = price_element.get_text(strip=True)
    print(price)
else:
    print("Price not found")
