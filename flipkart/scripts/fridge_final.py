from bs4 import BeautifulSoup
import requests
import csv
from csv import writer


check=1
start=1
end=40
page_no_list=list(range(start,end+1))

for page_number_test in page_no_list:

    url=f'https://www.flipkart.com/search?q=fridge&sid=j9e%2Cabm%2Chzg&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_6_na_na_na&as-pos=2&as-type=HISTORY&suggestionId=fridge%7CRefrigerators&requestId=8aedf69f-392f-494f-aa03-1871a56ceea5&page={page_number_test}'
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
        cell.append("Rs. " + price.text[1:])

        link_of_image=item.find('img',class_='_396cs4 _3exPp9')
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
                cell.append("")
            else:
                firstFlag = True
            cell.append(spec.text)
            list_of_rows.append(cell)
        list_of_rows.append(["", "", "", ""])

    with open('fridge_final.csv', 'a', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title","Rating","Price","Link", "Specifications"])
        writer.writerows(list_of_rows)
    file.close()

