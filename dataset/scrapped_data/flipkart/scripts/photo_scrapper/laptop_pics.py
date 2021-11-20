import requests
from bs4 import BeautifulSoup
import csv
from csv import writer
import os

start=1
end=30

page_no_list=list(range(start,end+1))

check=1

url='https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&page=2'
page=requests.get(url) 

print(check)
check=check+1

soup=BeautifulSoup(page.content,'html.parser')
images=soup.find_all('img', class_='_396cs4 _3exPp9')
number_of_images=1
for image in images:
    name=image['alt']
    link=image['src']
    print(number_of_images)
    number_of_images=number_of_images+1
    with open(name.replace(' ', '-' ).replace('/','') + '.jpg', 'wb') as file:
        im=requests.get(link)
        file.write(im.content)    
    file.close()
