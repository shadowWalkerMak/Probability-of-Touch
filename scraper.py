import requests
from bs4 import BeautifulSoup

# get the historical volatility of HSI from the web site investing.com
url = "https://www.investing.com/indices/hsi-volatility-historical-data"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
result = soup.find("div", attrs={"data-test": "instrument-header-details"})
result = result.text
result = float(result[:4])
hv = (result) / 100

# get the HSI last price from investing.com
url2 = "https://www.investing.com/indices/hang-sen-40"
page2 = requests.get(url2)
soup2 = BeautifulSoup(page2.content, "html.parser")
result2 = soup2.find("div", attrs={"data-test": "instrument-header-details"})
result2 = result2.text
# get all the string before .
lastPrice = result2[: result2.index(".")]
# get rid of ,
lastPrice = lastPrice.replace(",", "")
# convert the lastPrice from string to float
lastPrice = float(lastPrice)
