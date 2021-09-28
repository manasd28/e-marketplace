from bs4 import BeautifulSoup
import requests
import csv
from csv import writer


check=1
start=1
end=400
page_no_list=list(range(start,end+1))

for page_number_test in page_no_list:

    url=f'https://www.flipkart.com/search?q=mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=mobiles%7CMobiles&requestId=cd12ed0d-8da9-4775-a2d5-e42ca293eb08&as-searchtext=mob&page={page_number_test}'
    page=requests.get(url) 
    
    print(check)
    check=check+1

    soup=BeautifulSoup(page.content, 'html.parser')

    # information in html of site
    #print(soup)

    items=soup.findAll('a',class_="_1fQZEK")

    list_of_rows = []
    for item in items:
        cell = []

        # title of product
        title = item.find('div', attrs={ 'class': '_4rR01T'})
        cell.append(title.text)
        # rating of product
        rating=item.find('div',attrs={'class':'_3LWZlK'})
        try:
            rating_final=rating.get_text() 
        except AttributeError:
            rating_final=''
        cell.append(rating_final)
        # price of product

        price = item.find('div', attrs={ 'class': '_30jeq3 _1_WHN1'})
        try:
            price_final=price.get_text()
        except AttributeError:
            price_final=''
        cell.append(price_final)

        link_of_image=item.find('img', class_='_396cs4 _3exPp9')
        link=link_of_image['src']
        cell.append(link)

        specs = item.findAll('li', attrs={ 'class': 'rgWa7D'})
        # specs of product
        firstFlag = False
        for spec in specs:
            if firstFlag:
                cell = []
                cell.append("")
                cell.append("")
                cell.append("")
            else:
                firstFlag = True
            cell.append(spec.text)
            list_of_rows.append(cell)
        list_of_rows.append(["", "", ""])

    with open('mobiles2_final.csv', 'a', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title","Rating","Price","Link", "Specifications"])
        writer.writerows(list_of_rows)
    file.close()

