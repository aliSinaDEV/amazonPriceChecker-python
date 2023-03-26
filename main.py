import requests
import smtplib
from bs4 import BeautifulSoup

DESIRED_PRICE = 0.00
SENDER_EMAIL = "example@gmail.comm"
SENDER_PASSWORD = "PASSWORD"

RECEIVER_EMAIL = "example@gmail.com"


url = "https://www.amazon.com/dp/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Accept-Language": "Accept-Language: en-US"
}
response = requests.get(url, headers=headers)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
product_price = float(soup.find("span", class_="a-offscreen").text.replace('$',''))



if product_price <= DESIRED_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=RECEIVER_EMAIL,
            msg=f"the price for the product is {product_price}, click here to visit -> {url}"
        )
        connection.close()

        print("Email Sent!")
