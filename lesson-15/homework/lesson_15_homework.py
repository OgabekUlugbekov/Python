# 1. Task: Web Scraping with BeautifulSoup
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
headings = soup.find_all("h1")
for heading in headings:
    print(heading.text)

# 2. Task: Scraping Product Information
import requests
from bs4 import BeautifulSoup

url = "https://example.com/products"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
products = soup.find_all("div", class_="product")
for product in products:
    name = product.find("h2").text
    price = product.find("span", class_="price").text
    print(f"Product: {name}, Price: {price}")

# 3. Task: Scraping News Headlines
import requests
from bs4 import BeautifulSoup

url = "https://example.com/news"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")
for article in articles:
    headline = article.find("h2").text
    date = article.find("span", class_="date").text
    print(f"Headline: {headline}, Date: {date}")

# 4. Task: Scraping and Saving to CSV
import requests
from bs4 import BeautifulSoup
import csv

url = "https://example.com/data"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
rows = soup.find_all("tr")
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for row in rows:
        cols = row.find_all("td")
        data = [col.text for col in cols]
        writer.writerow(data)