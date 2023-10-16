import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.com/-/zh/dp/B07XXCHGXM/ref=sr_1_3?c=ts&keywords=%E5%AE%B6%E5%BA%AD%E6%90%85%E6%8B%8C%E6%9C%BA&qid=1697421918&s=kitchen&sr=1-3&ts_id=289929&th=1"
header = {
    'User-Agent': "imworthitaowu",
    'Accept-Language': "imworthitaowu",
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

