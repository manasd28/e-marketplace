import os
import pandas as pd

files = os.listdir('./')

try:
    os.mkdir('images')
except:
    pass


for f in files:
    if f.endswith('.csv'):
        df = pd.read_csv(f)
        df['path'] = pd.NA
        cnt = 0
        for ind, row in df.iterrows():
            if cnt%10:
                print(f'Done objects {cnt}')
            path = 'images/'+str(ind)+'.png'
            cmd = 'curl {} -o {}'.format(str(row['img']), path)
            os.system(cmd)
            df['path'][ind] = path
            cnt+=1
        df.to_csv(f)
