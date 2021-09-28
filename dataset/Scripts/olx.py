import scrapy
import json
import csv
from scrapy.crawler import CrawlerProcess

class olx(scrapy.Spider):
    name = 'olx_laptop_scrapper'
    
    url = 'https://www.olx.in/api/relevance/v2/search?facet_limit=100&lang=en&location=4058659&location_facet_limit=20&page=1&platform=web-mobile&query=laptops&spellcheck=true&user=17bcb4ef84ex75958c08'
    
    headers = {
            'user-agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Mobile Safari/537.36'
        }
    

    def __init__(self):
        with open('results.csv', 'w') as csv_file:
            csv_file.write('title,description,location,features,date,price\n')
    
    def start_requests(self):
        
        for page in range(0, 50):
            #print(self.url[:107] + '&page=' + str(1) + self.url[114:])
            yield scrapy.Request(url=self.url[:107] + '&page=' + str(page) + self.url[114:], headers=self.headers, callback=self.parse)
    
    def parse(self, res):
        data = res.text
        data = json.loads(data)
        
        for offer in data['data']:
            items = {
                'title': offer['title'],
                'description': offer['description'].replace('\n', ' '),
                'date': offer['display_date'],
                'price': offer['price']['value']['display']
            }
            
            print(json.dumps(items, indent=2))
            
            with open('results.csv', 'a') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=items.keys())
                writer.writerow(items)
    
    

# run scraper
process = CrawlerProcess()
process.crawl(olx)  
process.start()
