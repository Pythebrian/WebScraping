from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

out_filename = "graphics_cards.csv"
# header of csv file to be written
headers = "Brand,Product name, Shipping, Price \n"

# opens file, and writes headers
f = open(out_filename, "w")
f.write(headers)

"""
This short program will web scrape NewEgg. Currently it will only scrape one page. 
It will return the brand, price, shipping and item name all at once. It will also
export the collected information to an excel file

This code was inspired by a tutorial on YouTube on how to use beautifulsoup!
You can scrape different section of NewEgg by changing my_url below by pasting a new url in between the ''.
"""

my_url='https://www.newegg.ca/p/pl?N=100007708%2050001312%2050001314%2050001315%204814%20601201888%20601296707%20601331379%20600007787%20600358543%20600494828%20601303641%20600030348%20600100181'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")
containers = page_soup.findAll("div", {"class" : "item-container"})

for container in containers:
    brand_tag = container.find("div", "item-branding")
    brand_name = brand_tag.a.img["title"]

    gpu_name = container.find("a", {"class" : "item-title"})
    gpuname = gpu_name.text

    prize = container.find("div", {"class" : "item-action"})
    number_prize = prize.strong.text
    number_prize = "$" + number_prize
    shipping_tag = container.find("li", {"class" : "price-ship"})
    shipping = shipping_tag.text.strip()
    
    print ("Brand: " + brand_name + "\n")
    print ("GPU: " + gpuname + "\n")
    print ("Prize: $" + number_prize + "\n")
    print ("Shipping: " + shipping + "\n")
    f.write(brand_name + ", " + gpuname.replace(",", "|") + ", " + shipping + ", " + number_prize + "\n")





f.close() 
