import bs4
import requests
from bs4 import BeautifulSoup

carslist = []
priceslist = []
distancelist = []
detailslist = []
links = []
dev = []
descriptionlist = []

url = 'https://www.olx.com.eg/en/vehicles/cars-for-sale/q-verna/'
url2 = 'https://www.olx.com.eg/en/vehicles/cars-for-sale/q-verna/?page=2'
mainlink = [url,url2]


for i in range(len(mainlink)):
    session = requests.session()
    page = session.get(url)

    src = page.content
     #src = page2.content


    soup = bs4.BeautifulSoup(page.content, "html.parser")

    #get the availble cars and print it
    cars = soup.find_all("div",{"class":"a5112ca8"})



    for i in range(len(cars)):
        carslist.append(cars[i].text)

    print(carslist,"\n")



    #get the prices of cars and print it
    prices = soup.find_all("div",{"class":"_52497c97"})
    #dev = soup.find_all("div",{"class":"_41d2b9f3"})
    for i in range(len(prices)):
        #dev.append(dev[i])
        priceslist.append(prices[i].text)
        #links.append(dev[i].find("a").get("href"))

    print(priceslist, "\n")




    #get the distance travlled and print it
    distance = soup.find_all("div",{"class":"a8f6df88"})

    for i in range(len(distance)):

        distancelist.append(distance[i].text)

    print(distancelist)





    url = url2


dev = soup.find_all("div",{"class":"_41d2b9f3"})
for i in range(len(priceslist)):
    dev.append(dev[i])

    links.append(dev[i].find("a").get("href"))

for i in range(len(links)):
    links[i] = "https://www.olx.com.eg/" + links[i]

print(links)
for i in links:
    result = requests.get(i)
    src = result.content
    soup = bs4.BeautifulSoup(src, "html.parser")
    details = soup.find("div", {"class": "_59317dec"})
    description = soup.find("div", {"class": "_0f86855a"})
    descriptionlist.append(description.text)
    detailslist.append(details.text)
print(detailslist, "\n")
print(descriptionlist)