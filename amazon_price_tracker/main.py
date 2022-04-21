import requests
from bs4 import BeautifulSoup
import smtplib

my_email = "soumyachandraprabash@gmail.com"
password = "Chiranthna*123"


URL = "https://www.amazon.ae/Black-Decker-Multi-function-Vertical-Chopper/dp/B08BK9416D?ref=dlx_16566_sh_dcl_img_1_469fa452_dt_mese4_67"
headers = {
"Accept-Language": "en-US,en;q=0.9,ar;q=0.8",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
}
response = requests.get(url=URL,headers=headers)
product_page = response.text

soup = BeautifulSoup(product_page,'html.parser')
# print(soup.prettify())
price_text = soup.find(name="span",class_="a-offscreen")
product_title = (soup.find(name="span",class_="a-size-large product-title-word-break")).get_text()
print(product_title)
price_deal = float((price_text.get_text()).split('AED')[1])
print(price_deal)
target_price = 120.00

if price_deal < target_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="soumyaprabash@yahoo.com",
            msg=f"Amazon Price Alert \n\n{product_title} is now {price_deal}\n\n{URL}"
        )
