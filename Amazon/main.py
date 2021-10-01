import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver

import pandas as pd
import os
driver = webdriver.Chrome()



def imagedown(url, folder):

    try:
        if os.path.exists(folder):
            os.chdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    images = soup.find_all('img', {'class': 's-image'})
    number_of_image = 1
    for image in images:
        name = image['alt']
        link = image['src']
        print('number_of_pic: ', number_of_image)
        number_of_image = number_of_image + 1
        with open(name.replace(' ', '-').replace('/', '').replace('|', '-').replace('"', '-').replace('.', '-').replace(',', '-') + '.jpg', 'wb') as file:
            im = requests.get(link)
            file.write(im.content)
            print('Writing: ', name)



def get_url(search_term):
    template = "https://www.amazon.in/s?k={}&page="
    search_term = search_term.replace(' ', '+')
    url = template.format(search_term)
    url += '{}'
    return url


def extract_record(item):
    atag = item.h2.a
    desc = atag.text.strip()
    image = item.find('img', {'class': 's-image'})
    link = image['src']
    name = image['alt']

    try:
        price_parent = item.find('span', {'class': 'a-price'})
        price = price_parent.find('span', {'class': 'a-offscreen'}).text
    except AttributeError:
        return
    try:
        rating = item.find('i', {'class': 'a-icon a-icon-star-small a-star-small-4 aok-align-bottom'}).text
    except AttributeError:
        rating = " "

    result = (desc, price, rating, link)
    return result


def main(search_term):
    """run the main program here"""
    records = []
    url = get_url(search_term)
    os.mkdir(os.path.join(os.getcwd(), 'images_digitalcam'))
    for page in range(1, 21):
        driver.get(url.format(page))
        imagedown(url.format(page),'images_digitalcam')
        soup = bs(driver.page_source, 'html.parser')
        results = soup.find_all('div', {'data-component-type': "s-search-result"})

        for item in results:
            record = extract_record(item)
            if record:
                records.append(record)
    return records


x = main('digitalcamera')

df = pd.DataFrame(x, columns=["PRODUCT NAME", "PRODUCT PRICE", "PRODUCT RATING", "URL"])

print(df)

df.to_csv('digitalcamera.csv', index=False)
