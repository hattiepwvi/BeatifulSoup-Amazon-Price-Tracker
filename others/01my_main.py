import requests
from bs4 import BeautifulSoup
from pprint import pprint
from lxml import etree

URL= "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

HEADERS = {
    'Accept-Language': "imworthitaowu",
    'User-Agent': "imworthitaowu",
}

response = requests.get(url=URL, headers=HEADERS)

soup = BeautifulSoup(response.text, "html.parser")
prices = soup.select(".a-price-whole")
for price in prices:
    pprint(price.getText())

price = soup.find(class_="a-price-whole").getText()
pprint(price)


