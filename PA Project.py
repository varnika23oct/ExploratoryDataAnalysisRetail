
# coding: utf-8

# In[235]:


import pandas as pd
import numpy as np
from pandas import DataFrame,Series
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
pd.options.display.max_columns = 999
import warnings
warnings.filterwarnings("ignore")
data = pd.read_csv('korea data.csv')


# In[236]:


data.head()


# In[237]:


data.shape


# In[238]:


data.columns.tolist()


# In[239]:


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


# In[240]:


data_filtered.head()


# In[241]:


stores = data_filtered['Store Name'].unique().tolist()


# In[242]:


for i in range(5):
    print(stores[i],data_filtered[(data_filtered['Discount'].values <0) & (data_filtered['Store Name'] == stores[i])].shape[0])


# In[243]:


data_filtered.head()


# In[244]:


data_filtered.isnull().sum().sort_values(ascending = False)


# In[245]:


data['Outlook'].value_counts()


# In[246]:


data_filtered['Outlook'][data_filtered['Outlook'] == 'rainy'] = 'Rainy'

data_filtered['Outlook'][data_filtered['Outlook'] == 'cloudy'] = 'Cloudy'


# In[247]:


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


# In[248]:


data_filtered.head()


# In[249]:


data_filtered.info()


# In[250]:


data_filtered=data_filtered[data_filtered['Discount']>=0]


# In[ ]:



    


# In[251]:


data_filtered['SalesOnDiscPerc'] =(data_filtered['Discount']/data_filtered['Total Sales'])*100


# In[252]:


data_filtered['SalesOnDiscPerc'] = data_filtered['SalesOnDiscPerc'].astype('int64')


# In[253]:


data_filtered.shape


# In[254]:


data_filtered.head()


# In[255]:


data_filtered.columns.tolist()


# In[256]:


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


# In[257]:


data_filtered.shape


# In[258]:


storeB = data_filtered[data_filtered['Store Name'] == 'Store B']
storeA = data_filtered[data_filtered['Store Name'] == 'Store A']
storeC = data_filtered[data_filtered['Store Name'] == 'Store C']
storeD = data_filtered[data_filtered['Store Name'] == 'Store D']
storeE = data_filtered[data_filtered['Store Name'] == 'Store E']


# In[259]:


storeA.to_csv('storeA.csv', sep=',',index = False) 
storeB.to_csv('storeB.csv', sep=',',index = False) 
storeC.to_csv('storeC.csv', sep=',',index = False) 
storeD.to_csv('storeD.csv', sep=',',index = False) 
storeE.to_csv('storeE.csv', sep=',',index = False) 


# In[167]:


for i in range(5):
    print(stores[i],data[data['Store Name'] == stores[i]]['Distance from Station Y(Meter)'].unique())


# In[168]:


data.columns


# In[169]:


a = data['Distance from Station X(Meter)'].unique()


# In[170]:


data['Distance from Station Y(Meter)'].unique()


# In[171]:


a = [500, 550,550, 300, 600]


# In[172]:


b = [500, 550, 550,300, 600]


# In[173]:


plt.scatter(x = a,y = b)


# In[174]:


data_filtered.groupby(['Store Name','Holiday'])['Total Sales'].sum().unstack().T


# In[175]:


data_filtered.head()


# In[176]:


data_filtered['Outlook'].value_counts()


# In[178]:


data_filtered.groupby(['Outlook'])['Total Sales'].mean().plot(kind = 'bar')

stores


# In[179]:


data_filtered.groupby(['Store Name','Outlook'])['Total Sales'].mean().unstack(level = 0)['Store A'].values


# In[180]:


data_filtered.groupby(['Store Name','Outlook'])['Total Sales'].mean().unstack(level = 0)


# In[181]:


data_filtered.groupby(['Store Name'])['Total Sales'].sum().sort_values(ascending = False)


# In[182]:


fig, axs = plt.subplots(2,3, figsize=(15, 6), facecolor='w', edgecolor='k',sharey=True)
# fig.subplots_adjust(hspace = .5, wspace=.001)

axs = axs.ravel()

for i in range(5):
#     sns.barplot(data = data_filtered[data_filtered['Store Name'] == stores[i]].groupby(['Outlook'])['Total Sales'].mean(),ax=axs[i])
    sns.barplot(x = data_filtered.groupby(['Store Name','Outlook'])['Total Sales'].mean().unstack(level = 0)[stores[i]].index,ax = axs[i],y = data_filtered.groupby(['Store Name','Outlook'])['Total Sales'].mean().unstack(level = 0)[stores[i]].values)
#     axs[i].plot(kind = 'bar',)


# In[183]:


fig, axs = plt.subplots(2,3, figsize=(15, 6), facecolor='w', edgecolor='k',sharey=True)
# fig.subplots_adjust(hspace = .5, wspace=.001)

axs = axs.ravel()

for i in range(5):
#     sns.barplot(data = data_filtered[data_filtered['Store Name'] == stores[i]].groupby(['Outlook'])['Total Sales'].mean(),ax=axs[i])
    sns.barplot(x = data_filtered.groupby(['Store Name','Holiday'])['Total Sales'].mean().unstack(level = 0)[stores[i]].index,ax = axs[i],y = data_filtered.groupby(['Store Name','Holiday'])['Total Sales'].mean().unstack(level = 0)[stores[i]].values)
#     axs[i].plot(kind = 'bar',)


# In[184]:


fig, axs = plt.subplots(2,3, figsize=(15, 6), facecolor='w', edgecolor='k',sharey=True)
# fig.subplots_adjust(hspace = .5, wspace=.001)

axs = axs.ravel()

for i in range(5):
#     sns.barplot(data = data_filtered[data_filtered['Store Name'] == stores[i]].groupby(['Outlook'])['Total Sales'].mean(),ax=axs[i])
    sns.barplot(x = data_filtered.groupby(['Store Name','Month'])['Total Sales'].sum().unstack(level = 0)[stores[i]].index,ax = axs[i],y = data_filtered.groupby(['Store Name','Month'])['Total Sales'].sum().unstack(level = 0)[stores[i]].values)
#     axs[i].plot(kind = 'bar',)


# In[185]:


# storeB_JT['Outlook'][storeB_JT['Outlook'] == 'rainy'] = 'Rainy'

# storeB_JT['Outlook'][storeB_JT['Outlook'] == 'cloudy'] = 'Cloudy'


# In[186]:


# most correlated features
import seaborn as sns
corrmat = storeB.corr()
plt.figure(figsize = (15,7))
# or fig, ax = plt.subplots(figsize=(20, 10))
# top_corr_features = corrmat.index[abs(corrmat["Total Sales"])>0.1]
g = sns.heatmap(corrmat,annot=True,cmap="RdYlGn")
# g = sns.heatmap(corrmat,annot=True,cmap="RdYlGn")

#g = sns.heatmap(corrmat,annot=True,cmap="RdYlGn")


# In[190]:


fig, axs = plt.subplots(5,1, figsize=(20, 30), facecolor='w', edgecolor='k',sharey=True)
# fig.subplots_adjust(hspace = .5, wspace=.001)

axs = axs.ravel()

for i in range(5):
#     sns.barplot(data = data_filtered[data_filtered['Store Name'] == stores[i]].groupby(['Outlook'])['Total Sales'].mean(),ax=axs[i])
    corrmat = data_filtered[data_filtered['Store Name'] == stores[i]].corr()

    g = sns.heatmap(corrmat,annot=True,cmap="RdYlGn",ax = axs[i])

#     axs[i].plot(kind = 'bar',)


# In[45]:


data.shape


# In[46]:


data[data['Discount'].values <0].shape


# In[47]:


storeB.groupby(['Outlook']).mean()['Total Sales'].plot(kind = 'bar')


# In[49]:


storeA.groupby(['Month']).mean()['Total Sales'].plot(kind = 'bar')

