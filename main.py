from bs4 import BeautifulSoup
import requests

product_url = "https://www.amazon.com/Passport-Portable-External-Drive-Black/dp/B07VTW2LPX"
header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"
}

response = requests.get(product_url, headers=header)
response.raise_for_status()
result = response.content

soup = BeautifulSoup(result, "lxml")
price = soup.find(id="priceblock_ourprice").getText()
price_without_currency = float(price.split("$")[1])
print(price_without_currency)
