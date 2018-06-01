

import pandas as pd
import numpy as np
from pandas import DataFrame,Series
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
pd.options.display.max_columns = 999
import warnings
warnings.filterwarnings("ignore")
data = pd.read_csv('korea data.csv')

data.head()

data.shape

data.columns.tolist()

data_filtered = data[[
 'Store Name',
 'Date',
 '# of Customers',
 '# of Items',
 'Total Sales',
 'Discount',
    'Month',
 'Weekday',
 'Distance from Station X(Meter)',
 'Distance from Station Y(Meter)',
 'Distance from Main Street(Meter)',
 'YenWonRatio',
 'Holiday',
 'ActualHighTemp',
 'Outlook',
 'Japanese Tourists']]
 
 data_filtered.head()
 
 stores = data_filtered['Store Name'].unique().tolist()
 
 for i in range(5):
    print(stores[i],data_filtered[(data_filtered['Discount'].values <0) & (data_filtered['Store Name'] == stores[i])].shape[0])

#Checking for Null Values  
data_filtered.isnull().sum().sort_values(ascending = False)

data['Outlook'].value_counts()

#Transforming duplicate data
data_filtered['Outlook'][data_filtered['Outlook'] == 'rainy'] = 'Rainy'
data_filtered['Outlook'][data_filtered['Outlook'] == 'cloudy'] = 'Cloudy'


data_filtered = data_filtered[['Store Name',
 'Discount',
 'Date',
 'Month',
 'Weekday',
 'YenWonRatio',
 'Holiday',
 'ActualHighTemp',
 'Outlook',
 'Japanese Tourists',
    'Total Sales']]


data_filtered.head()

data_filtered.info()

#Creating Discount Percent attribute
data_filtered=data_filtered[data_filtered['Discount']>=0]
data_filtered['SalesOnDiscPerc'] =(data_filtered['Discount']/data_filtered['Total Sales'])*100


data_filtered = data_filtered[['Store Name',
 'Month',
 'Date',
 'Weekday',
 'YenWonRatio',
 'Holiday',
 'ActualHighTemp',
 'Outlook',
 'Japanese Tourists',
 'Discount',
 'SalesOnDiscPerc', 
 'Total Sales'
]]
data_filtered['SalesOnDiscPerc'] = data_filtered['SalesOnDiscPerc'].astype('int64')

#Extrating data for different store and creating different csv file for them
storeB = data_filtered[data_filtered['Store Name'] == 'Store B']
storeA = data_filtered[data_filtered['Store Name'] == 'Store A']
storeC = data_filtered[data_filtered['Store Name'] == 'Store C']
storeD = data_filtered[data_filtered['Store Name'] == 'Store D']
storeE = data_filtered[data_filtered['Store Name'] == 'Store E']


storeA.to_csv('storeA.csv', sep=',',index = False) 
storeB.to_csv('storeB.csv', sep=',',index = False) 
storeC.to_csv('storeC.csv', sep=',',index = False) 
storeD.to_csv('storeD.csv', sep=',',index = False) 
storeE.to_csv('storeE.csv', sep=',',index = False) 
