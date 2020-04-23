from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from time import localtime, strftime  
import datetime 
import csv
now = datetime.datetime.now()
"""
This program will allow you will find out real time stock price from the TMX website.
As long as this program is running, the stock price will update as soon as a new price
is found on the website!

Change the url in parseprice() to track the stock you want!

I am currently working to export the collected stock prices into a csv file to do more finanical analysis!
"""

out_filename = "RTSQ.csv"
# header of csv file to be written
headers = "Stock Symbol, Stock Price\n"

# opens file, and writes headers
f = open(out_filename, "w")
f.write(headers)


def parseprice():
    url = "https://web.tmxmoney.com/quote.php?locale=en&qm_symbol=AC"
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    quotes = page_soup.find("div", {"class" : "labs-symbol"})
    price = quotes.span.span.text
    return price

def parseticker():
    url = "https://web.tmxmoney.com/quote.php?locale=en&qm_symbol=AC"
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    quotes = page_soup.find("div", {"class" : "labs-symbol"})
    ticker = quotes.text.strip()
    result = ticker.replace("\t", "")
    return result[:4]

stored_price = 0
count = 0
price_list = []
while True:
    if stored_price == parseprice():
        continue
    else:
        print ("The current price is: " + str(parseprice()) + "      " + strftime("%Y-%m-%d %H:%M:%S", localtime()))
        stored_price = parseprice()
    price_list.append(parseprice())
   

f.write(price_list[0] + "\n")
