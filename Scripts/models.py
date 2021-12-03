import pandas  as pd
import numpy as np
import xgboost
import pickle
import random

# LAPTOP MODEL CREATION
# df1 = pd.read_csv('/home/manasd28/Desktop/e-marketplace/dataset/cleansed_data/amazon/laptop.csv').iloc[:, 1:]
# df2 = pd.read_csv('/home/manasd28/Desktop/e-marketplace/dataset/cleansed_data/flipkart/laptop.csv').iloc[:, 1:]
# df1['display'] = np.nan
# df2['graphic_card'] = np.nan

# df2 = df2[['Title', 'Price', 'Rating', 'Link', 'Company', 'Processor',
#        'ssd', 'hdd', 'ram', 'graphic_card', 'Display']]

# columns = ['title', 'price', 'rating', 'url', 'brand', 'processor', 'ssd', 'hdd', 'ram', 'graphic_card', 'display']
# df1.columns = columns
# df2.columns = columns
# df1['source'] = 'amazon'
# df2['source'] = 'flipcart'

# df = df1.append(df2).replace([' ', ''], np.nan)

# df['rating'] = df['rating'].apply(lambda x: round(np.random.normal(3, 0.8), 1) if x!=x else x)
# df = df.applymap(lambda s: s.lower() if type(s) == str else s).iloc[:,:-3]
# df.drop(['title', 'url'], axis=1, inplace=True)

# df = pd.get_dummies(df, columns = ['processor', 'brand'], drop_first=True)

# from sklearn.svm import SVR
# from sklearn.neighbors import KNeighborsRegressor
# from sklearn.linear_model import Lasso
# from sklearn.neighbors import kNeighborClassifier

# # regressor = SVR()
# # regressor = KNeighborsRegressor(10)
# regressor = Lasso(max_iter=100000)

# classifier = kNeighborClassifier()

# y = df.iloc[:,0]
# X = df.iloc[:,2:5]

# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y)

# regressor.fit(X_train, y_train)
# y_pred = regressor.predict(X_test)

# from sklearn.metrics import mean_squared_error
# print(np.sqrt(mean_squared_error(y_test, y_pred)))

# # pickle.dump(regressor, open('laptop-model.pkl', 'wb'))

# MOBILE MODEL CREATION
df1 = pd.read_csv('../dataset/cleansed_data/flipkart/phone.csv').iloc[:,2:]
df2 = pd.read_csv('../dataset/cleansed_data/amazon/phone.csv').iloc[:,2:]
displays = [ 6.53 ,  6.5  ,  6.6  ,  6.78 ,  6.82 ,  6.52 ,  6.1  ,
        1.77 ,  6.515,  6.4  ,  6.51 ,  2.8  ,  6.22 ,  5.4  ,  1.8  ,
        6.517,  6.67 ,  2.4  ,  5.45 ,  2.6  ,  6.08 ,  0.66 ,  6.58 ,
        4.7  ,  6.43 ,  1.7  ,  6.62 ,  1.44 ,  6.95 ,  1.4  ,  6.7  ,
        6.55 ,  5.7  ,  1.54 ,  6.088,  6.8  ,  6.44 ,  5.   ,  6.3  ,
        6.39 ,  2.2  ,  5.81 ,  5.5  ,  6.26 ,  3.5  ,  6.56 ,  6.49 ,
        6.9  ,  6.19 ,  6.2  ,  6.   ,  1.3  ,  1.75 ,  5.71 , 66.   ,
        7.6  ,  2.   ,  5.99 ,  6.65 ,  6.57 ,  6.102,  6.35 ]
price_values = {1:16, 2:32, 3:64, 4:128, 5:256, 6:512}
df2['budget'] = pd.qcut(df2['PRODUCT PRICE'], 6, [1,2,3,4,5,6])
df2['storage'] = df2['budget'].map(price_values)
df2['display'] = [random.choices(displays)[0] for i in range(len(df2))]
df2 = df2[['PRODUCT RATING', 'URL', 'display', 'brand', 'PRODUCT PRICE', 'storage', 
          'ram', 'rom']]
df1.drop('Battery', axis = 1, inplace = True)
df2['source'] = 1
df1['source'] = 0
columns = ['rating', 'url', 'display', 'brand', 'price', 'storage', 'ram', 'rom', 'source']
df1.columns = columns
df2.columns = columns
df = df1.append(df2)
df['rating'] = df['rating'].apply(lambda x: round(np.random.normal(3, 0.8), 1) if x!=x else x)
df = df.applymap(lambda s: s.lower() if type(s) == str else s)
up = np.quantile(df.price, 0.75)
lb = np.quantile(df.price, 0.25)
df['budget'] = df['price'].apply(lambda x: 'low' if x<lb else 'medium' if x<up else 'high')
df = df[['storage', 'ram', 'rom','price']].fillna(method='ffill')
X = df.iloc[:, :3]
y = df.iloc[:,-1]

from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import Lasso

# regressor = SVR()
# regressor = KNeighborsRegressor(10)
regressor = Lasso(max_iter=100000)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y)

regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

from sklearn.metrics import mean_squared_error
print(np.sqrt(mean_squared_error(y_test, y_pred)))

# pickle.dump(regressor, open('phone-model.pkl', 'wb'))
