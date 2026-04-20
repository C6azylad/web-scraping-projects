import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1
}

response = requests.get(url, params=params)
data = response.json()

coins = []

for coin in data:
    coins.append({
        "Name": coin["name"],
        "Symbol": coin["symbol"].upper(),
        "Price (USD)": coin["current_price"],
        "Market Cap": coin["market_cap"],
        "24h Change %": coin["price_change_percentage_24h"]
    })

df = pd.DataFrame(coins)

print(df)

df.to_csv("crypto_prices.csv", index=False)
print("\nDone! Saved to crypto_prices.csv")