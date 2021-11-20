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
    end=70

    page_no_list=list(range(start,end+1))

    check=1
    os.mkdir(os.path.join(os.getcwd(),'tv_pics'))

    for page in page_no_list:


        url=f'https://www.flipkart.com/search?q=televisions&sid=ckf%2Cczl&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&as-pos=1&as-type=RECENT&suggestionId=televisions%7CTVs&requestId=b61f79c5-5aa4-48d5-ac54-b6038f437aae&as-searchtext=telev&page={page}'

        print('page_number= ',check)
        check=check+1
        imagedown(url,'tv_pics')

if __name__=='__main__':
    main()

