import scrapy
import json
import csv
from scrapy.crawler import CrawlerProcess

class olx(scrapy.Spider):
    name = 'olx_mobile_scrapper'
    
    url = 'https://www.olx.in/api/relevance/v2/search?facet_limit=100&isSearchCall=true&lang=en&location=1000001&location_facet_limit=20&page=2&platform=web-desktop&query=laptops&spellcheck=true&user=17c2669ca83x2d9787a6'
    
    headers = {
            'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0'
        }
    

    def __init__(self):
        with open('results.csv', 'w') as csv_file:
            csv_file.write('title,description,date,price,img\n')
    
    def start_requests(self):
        
        for page in range(0, 50):
            #print(self.url[:107] + '&page=' + str(1) + self.url[114:])
            yield scrapy.Request(url=self.url[:107] + '&page=' + str(page) + self.url[114:], headers=self.headers, callback=self.parse)
    
    def parse(self, res):
        data = res.text
        data = json.loads(data)
        
        for offer in data['data']:
            print()
            items = {
                'title': offer['title'],
                'description': offer['description'].replace('\n', ' '),
                'date': offer['display_date'],
                'price': offer['price']['value']['display'],
                'img': offer['images'][0]['url']
            }
            
            print(json.dumps(offer, indent=2))
            
            with open('results.csv', 'a') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=items.keys())
                writer.writerow(items)
    
    

# run scraper
process = CrawlerProcess()
process.crawl(olx)  
process.start()
