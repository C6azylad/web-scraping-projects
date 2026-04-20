import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

contacts = []

books = soup.find_all("article", class_="product_pod")

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.p["class"][1]
    
    contacts.append({
        "Business Name": title,
        "Price": price,
        "Contact Rating": rating,
        "Website": url
    })

df = pd.DataFrame(contacts)
df.to_csv("contacts.csv", index=False)

print(f"Done! Scraped {len(contacts)} contacts and saved to contacts.csv")