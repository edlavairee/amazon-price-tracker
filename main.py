import requests
from bs4 import BeautifulSoup
import smtplib

my_email = "edlavairepython@gmail.com"
password = "PythonCourse123!@#"

url = "https://www.amazon.com/Apple-iPad-10-2-inch-Wi-Fi-128GB/dp/B08J61NFNR/ref=sr_1_1_sspa?dchild=1&keywords=ipad&qid=1618199792&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExSE9WUDJPWlY1NlI2JmVuY3J5cHRlZElkPUEwMzYxODQxWUxKMkIyWk1MOEhRJmVuY3J5cHRlZEFkSWQ9QTA0MTU1MjczUTJXTDNTTDVHWFhYJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}
response = requests.get(url=url, headers=headers)
website_html = response.text

soup = BeautifulSoup(website_html, "lxml")
price = float(soup.find(name="span", class_="a-size-medium a-color-price priceBlockBuyingPriceString").text[1::])

email_price = '${:,.2f}'.format(price)
if price < 430:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="edlavairepython@gmail.com",
                            msg=f"Subject: Price Dropped - {email_price}!\n\n Click the link to go buy: \n{url}")
