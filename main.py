from bs4 import BeautifulSoup
import requests
import smtplib
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"

BUY_PRICE = 85

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
product_title = soup.find(id="productTitle").get_text().strip()


if price_without_currency < BUY_PRICE:
    message = f"{product_title} is now {price}"

    with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{product_url}"
        )
