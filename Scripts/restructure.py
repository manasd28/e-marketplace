import pandas as pd
import numpy as np
import re
import time

intel_processors = ['i3', 'i5', 'i7', 'i9', 'celeron']
amd_processors = ['ryzen 3', 'ryzen 5', 'ryzen 7', 'ryzen 9', 'amd athlon']
graphic_cards = ['rtx 3050', 'rtx 3060', 'mx350', 'gtx 1650', 'mx230', 'rtx 3050', 'mx450', 'mx230', 'vega 8', '1000m', 'gtx 1660', 'iris xe', 'intel integrated', 'amd radeon']
os = ['windows 10', 'dos', 'mac os', 'linux', 'ubuntu', 'chrome']

# Amazon

df = pd.read_csv('/home/manasd28/Desktop/workspace/laptops.csv')

def min_edit_dist(a, b):
    n = len(a)
    m = len(b)
    dp = np.zeros((n+1, m+1), dtype = float)
    for i in range(n+1):
        for j in range(m+1):
            if i==0:
                dp[i][j] = j
            elif j==0:
                dp[i][j] = i
            elif a[i-1]!=b[j-1]:
                dp[i][j] = min(min(dp[i-1][j], dp[i][j-1])+1, dp[i-1][j-1]+1.5)
            else:
                dp[i][j] = dp[i-1][j-1]
    return dp[n][m]

def extract_info(row):
    # Brand
    row['brand'] = row['PRODUCT NAME'].split()[0]
    
    # Processor
    processor_f = False
    
    row['PRODUCT NAME'] = row['PRODUCT NAME'].lower().replace(u'\xa0', u' ')
    for p in intel_processors:
        if(row['PRODUCT NAME'].find(p) != -1):
            row['processor'] = 'intel '+p
            processor_f = True
            break
    if processor_f == False:
        for p in amd_processors:
            if(row['PRODUCT NAME'].find(p) != -1):
                row['processor'] = p
                processor_f = True
                break
    if processor_f == False:
        row['processor'] = 'others'
    
    # SSD
    if row['PRODUCT NAME'].find('nvme') != -1:
        try:
            sp = float(re.findall('[a-zA-Z0-9\.]+\s*nvme', 
                                        row['PRODUCT NAME'])[0].split()[0][:-2])
            row['ssd'] = sp if sp>12 else sp*1024
        except Exception:
            row['ssd'] = 0
    elif row['PRODUCT NAME'].find('ssd')!=-1:
        try:
            sp = re.findall('[a-zA-Z0-9]+\s*ssd', row['PRODUCT NAME'])[0].split()[0]
            if(len(sp)>2 and sp.endswith('gb')):
                row['ssd'] = int(sp[:-2])
            elif(len(sp)>2 and sp.endswith('tb')):
                row['ssd'] = 1024*int(sp[:-2])
            else:
                sp = float(re.findall('[a-zA-Z0-9]+\s*[a-zA-Z0-9]+\s*ssd', 
                                row['PRODUCT NAME'])[0].split()[0])
                row['ssd'] = sp if sp>12 else sp*1024
        except Exception:
            row['ssd'] = 0
    else:
        row['ssd'] = 0
    
    # HDD
    if row['PRODUCT NAME'].find('hdd')!=-1:
        try:
            sp = re.findall('[a-zA-Z0-9]+\s*hdd', row['PRODUCT NAME'])[0].split()[0]
            if(len(sp)>2 and sp.endswith('gb')):
                row['hdd'] = int(sp[:-2])
            elif(len(sp)>2 and sp.endswith('tb')):
                row['hdd'] = 1024*int(sp[:-2])
            else:
                sp = float(re.findall('[a-zA-Z0-9]+\s*[a-zA-Z0-9]+\s*hdd', 
                                row['PRODUCT NAME'])[0].split()[0])
                row['hdd'] = sp if sp>12 else sp*1024
        except Exception:
            row['hdd'] = 0
    else:
        row['hdd'] = 0
    
    # RAM
    try:
        rm = sorted([sp.split()[0] if not sp.endswith('gb') else int(sp[:-2]) 
                      for sp in re.findall('[a-zA-Z0-9]+\s*gb', row['PRODUCT NAME'])])
        if len(rm)>1 and rm[1]<32:
            row['ram'] = rm[1]
        elif rm[0]<32:
            row['ram'] = rm[0]
        else:
            row['ram'] = 4
        
    except Exception:
        row['ram'] = 8
        
    # Graphic Crad
    mn = np.inf
    res = ""
    string = row['PRODUCT NAME']
    replace_chars = ['\(', '\)', '/']
    for ch in replace_chars:
        string = re.sub(ch, ' ', string)
    string = string.strip().split()
    for ch in string:
        for card in graphic_cards:
            dis = min_edit_dist(card, ch)
            if max(len(card), len(ch)) - dis>3:
                if mn>dis:
                    mn = dis    
                    res = card
    row['graphic_card'] = res
    
    # Price
    row['PRODUCT PRICE'] = re.sub('[^0-9]', '', row['PRODUCT PRICE'])
    
    # Rating
    row['PRODUCT RATING'] = row['PRODUCT RATING'][:3]
    
    return row

timeGC_0 = time.time()
df = df.apply(extract_info, axis = 1)
timeGC_1 = time.time()
print("Time preprocessing : ", timeGC_1 - timeGC_0)

# FLipcart

df = pd.read_csv('/home/manasd28/Desktop/workspace/laptop_new_cleansed.csv').iloc[:,:-1].drop(['SSD', 'RAM'], axis=1)

def extract_values(row):
    # Price
    row['Price'] = re.sub(r'[^0-9]', '', row['Price'])
    row['Title'] = row['Title'].lower()
    # Processor
    processor_f = False
    row['Processor'] = row['Processor'].lower().replace(u'\xa0', u' ')
    for p in intel_processors:
        if(row['Processor'].find(p) != -1):
            row['Processor'] = 'intel '+p
            processor_f = True
            break
    if processor_f == False:
        for p in amd_processors:
            if(row['Processor'].find(p) != -1):
                row['Processor'] = p
                processor_f = True
                break
    if processor_f == False:
        row['Processor'] = 'others'
    
    # Display
    try:
        row['Display'] = re.findall(r'\(.*\)', row['Display'])[0]
        row['Display'] = re.sub('[^0-9.]', '', row['Display'])
    except Exception:
        pass
    
    # SSD
    if row['Title'].find('nvme') != -1:
        try:
            sp = float(re.findall('[a-zA-Z0-9\.]+\s*nvme', 
                                        row['Title'])[0].split()[0][:-2])
            row['ssd'] = sp if sp>12 else sp*1024
        except Exception:
            row['ssd'] = 0
    elif row['Title'].find('ssd')!=-1:
        try:
            sp = re.findall('[a-zA-Z0-9]+\s*ssd', row['Title'])[0].split()[0]
            if(len(sp)>2 and sp.endswith('gb')):
                row['ssd'] = int(sp[:-2])
            elif(len(sp)>2 and sp.endswith('tb')):
                row['ssd'] = 1024*int(sp[:-2])
            else:
                sp = float(re.findall('[a-zA-Z0-9]+\s*[a-zA-Z0-9]+\s*ssd', 
                                row['Title'])[0].split()[0])
                row['ssd'] = sp if sp>12 else sp*1024
        except Exception:
            row['ssd'] = 0
    else:
        row['ssd'] = 0
    
    # HDD
    if row['Title'].find('hdd')!=-1:
        try:
            sp = re.findall('[a-zA-Z0-9]+\s*hdd', row['Title'])[0].split()[0]
            if(len(sp)>2 and sp.endswith('gb')):
                row['hdd'] = int(sp[:-2])
            elif(len(sp)>2 and sp.endswith('tb')):
                row['hdd'] = 1024*int(sp[:-2])
            else:
                sp = float(re.findall('[a-zA-Z0-9]+\s*[a-zA-Z0-9]+\s*hdd', 
                                row['Title'])[0].split()[0])
                row['hdd'] = sp if sp>12 else sp*1024
        except Exception:
            row['hdd'] = 0
    else:
        row['hdd'] = 0
    
    # RAM
    try:
        rm = sorted([sp.split()[0] if not sp.endswith('gb') else int(sp[:-2]) 
                      for sp in re.findall('[a-zA-Z0-9]+\s*gb', row['Title'])])
        if len(rm)>1 and rm[1]<32:
            row['ram'] = rm[1]
        elif rm[0]<32:
            row['ram'] = rm[0]
        else:
            row['ram'] = 4
        
    except Exception:
        row['ram'] = 8
    return row

df = df.apply(extract_values, axis = 1)
