import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.com/-/zh/dp/B07HC8MS3Z/ref=sbl_dpx_kitchen-mixers_B07XXCHGXM_0?th=1"
header = {
    'User-Agent': "imworthitaowu",
    'Accept-Language': "imworthitaowu",
}
my_email = "imworthitaowu"
password = "imworthitaowu"

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

try:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        if price_as_float < 100:
            connection.sendmail(
                from_addr=my_email,
                to_addrs="imworthitaowu@outlook.com",
                msg=f"Subject:Amazon Price Alert!\n\nNurxiovo 3 in 1 Stand Mixer 850W Kitchen Food Standing Mixer with 6 Speed and Pulse, Home mixer with 6.5 QT Stainless Steel Bowl, Dough Hook, Whisk, Beater, Meat Blender and Juice Extracter White is now ${price_as_float}\n{url}"
            )
except smtplib.SMTPException as e:
    print("An error occurred:", str(e))






