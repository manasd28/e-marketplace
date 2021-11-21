import pandas as pd
import numpy as np
import re

df = pd.read_csv('/home/manasd28/Desktop/e-marketplace/dataset/scrapped_data/amazon/Television/television.csv')

def extract_info(row):
    row['PRODUCT NAME'] = row['PRODUCT NAME'].lower()
    
    # Brand
    row['brand'] = row['PRODUCT NAME'].split()[0]
    
    # Screen Size
    x = row['PRODUCT NAME'].find('(')
    row['screen_size'] = (row['PRODUCT NAME'][x+1:x+3])
    
    # Resolution
    if '4k' in row['PRODUCT NAME']:
        row['4k'] = 1
    elif 'hd' in row['PRODUCT NAME']:
        row['hd'] = 1
    else:
        row['4k'] = 0
        row['hd'] = 0
    
    # Alexa
    if 'alexa' in row['PRODUCT NAME']:
        row['alexa'] = 1
    else:
        row['alexa'] = 0
        
    # Price
    row['PRODUCT PRICE'] = re.sub('[^0-9]', '', row['PRODUCT PRICE'])
    
    # Rating
    row['PRODUCT RATING'] = row['PRODUCT RATING'][:3]
    
    return row

df = df.apply(extract_info, axis = 1)
df.fillna(0, inplace = True)
df = df.sort_values('PRODUCT PRICE')
df.to_csv('tv.csv')