import pandas  as pd
import numpy as np
import xgboost
import pickle

df1 = pd.read_csv('/home/manasd28/Desktop/e-marketplace/dataset/cleansed_data/amazon/laptop.csv').iloc[:, 1:]
df2 = pd.read_csv('/home/manasd28/Desktop/e-marketplace/dataset/cleansed_data/flipkart/laptop.csv').iloc[:, 1:]
df1['display'] = np.nan
df2['graphic_card'] = np.nan

df2 = df2[['Title', 'Price', 'Rating', 'Link', 'Company', 'Processor',
       'ssd', 'hdd', 'ram', 'graphic_card', 'Display']]

columns = ['title', 'price', 'rating', 'url', 'brand', 'processor', 'ssd', 'hdd', 'ram', 'graphic_card', 'display']
df1.columns = columns
df2.columns = columns
df1['source'] = 'amazon'
df2['source'] = 'flipcart'

df = df1.append(df2).replace([' ', ''], np.nan)

df['rating'] = df['rating'].apply(lambda x: round(np.random.normal(3, 0.8), 1) if x!=x else x)
df = df.applymap(lambda s: s.lower() if type(s) == str else s).iloc[:,:-3]
df.drop(['title', 'url'], axis=1, inplace=True)

df = pd.get_dummies(df, columns = ['processor', 'brand'], drop_first=True)

from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import Lasso

# regressor = SVR()
# regressor = KNeighborsRegressor(10)
regressor = Lasso(max_iter=100000)

y = df.iloc[:,0]
X = df.iloc[:,2:5]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y)

regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

from sklearn.metrics import mean_squared_error
print(np.sqrt(mean_squared_error(y_test, y_pred)))
print(df.columns)

pickle.dump(regressor, open('laptop-model.pkl', 'wb'))
