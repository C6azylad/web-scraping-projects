import requests
from bs4 import BeautifulSoup
import pandas as pd

print("Step 1: Scraping data...")
url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

data = []
for book in books:
    title = book.h3.a["title"]
    price = float(book.find("p", class_="price_color").text.replace("£", "").replace("Â", ""))
    rating = book.p["class"][1]
    data.append({
        "Title": title,
        "Price (£)": price,
        "Rating": rating
    })

print(f"Scraped {len(data)} books!")

print("\nStep 2: Cleaning data...")
df = pd.DataFrame(data)
df = df.drop_duplicates()
df = df.dropna()
df["Rating"] = df["Rating"].replace({
    "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5
})
df = df.sort_values("Rating", ascending=False)
print("Data cleaned!")

print("\nStep 3: Exporting data...")
df.to_excel("final_output.xlsx", index=False)
df.to_csv("final_output.csv", index=False)
print("Saved to final_output.xlsx and final_output.csv")

print("\nDone! Full pipeline complete!")
print(df.head())