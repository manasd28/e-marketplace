import requests
from bs4 import BeautifulSoup
import csv
from csv import writer
import os


def imagedown(url,folder):
    
    try:
        if(os.path.exists(folder)):
            os.chdir(os.path.join(os.getcwd(),folder))
    except:
        pass
    r=requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    images=soup.find_all('img', class_='_396cs4 _3exPp9')
    number_of_image=1
    for image in images:
        name=image['alt']
        link=image['src']
        print('number_of_pic: ',number_of_image)
        number_of_image=number_of_image+1
        with open(name.replace(' ', '-' ).replace('/','').replace('|','-') + '.jpg', 'wb') as file:
            im=requests.get(link)
            file.write(im.content)
            print('Writing: ',name)

def main():
    start=1
    end=30

    page_no_list=list(range(start,end+1))

    check=1
    os.mkdir(os.path.join(os.getcwd(),'camera_pics'))

    for page in page_no_list:


        url=f'https://www.flipkart.com/search?q=camera&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={page}'

        print('page_number= ',check)
        check=check+1
        imagedown(url,'camera_pics')

if __name__=='__main__':
    main()

