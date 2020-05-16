from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from time import localtime, strftime  
import datetime 
import csv
import smtplib
now = datetime.datetime.now()



EMAIL_ADDRESS = "@gmail.com" #Sender
PASSWORD = ""   #Sender passcode
MY_EMAIL = "@gmail.com" #Recipient (Can be the same as sender)


def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ADDRESS, PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(EMAIL_ADDRESS, MY_EMAIL, message)
        server.quit()
        print("Email sent!")
    except:
        print("Email failed to send.")

subject = "Alarm"
msg = "Price reached set value of " + set_price



def parseprice():
    url = "https://web.tmxmoney.com/quote.php?locale=en&qm_symbol=AC" #Link to the tmx website, you can pick the stock you like
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
alarm = False

set_price = float(input("Alarm price: "))
while True:
    if stored_price == parseprice():
        continue
    else:
        print ("The current price is: " + str(parseprice()) + "      " + strftime("%Y-%m-%d %H:%M:%S", localtime()))
        stored_price = parseprice()
        if parseprice() == stored_price:
            send_email(subject, msg)
