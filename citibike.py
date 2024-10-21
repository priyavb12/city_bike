#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from pathlib import Path
import pandas as pd
pd.set_option('max_colwidth',400)


# In[2]:


#file to load

citi_bike_csv_load = Path('./Resources/JC-201908-citibike-tripdata.csv')


# In[3]:


#read csv

citi_bike_df = pd.read_csv(citi_bike_csv_load)
citi_bike_df.head()


# In[4]:


#find datatype in dataframe

citi_bike_df = pd.read_csv('./Resources/JC-201908-citibike-tripdata.csv')

print(type(citi_bike_df))


# In[5]:


citi_bike_df.dtypes


# In[6]:


#check for null values
citi_bike_df.isnull().sum()


# In[7]:


#check for duplicates

citi_bike_df.duplicated()


# In[8]:


citi_bike_df.duplicated().sum()


# In[9]:


citi_bike_df.columns =citi_bike_df.columns.str.replace(' ' ,'_')


# In[10]:


citi_bike_df.head()


# In[11]:


citi_bike_df['starttime'] = pd.to_datetime(citi_bike_df['starttime'])
citi_bike_df['starttime'] = citi_bike_df['starttime'].dt.strftime('%Y-%m-%d %H:%M:%S')


# In[12]:


citi_bike_df.tail()


# In[13]:


citi_bike_df['stoptime'] = pd.to_datetime(citi_bike_df['stoptime'])
citi_bike_df['stoptime'] = citi_bike_df['stoptime'].dt.strftime('%Y-%m-%d %H:%M:%S')


# In[14]:


citi_bike_df


# In[15]:


citi_bike_df = citi_bike_df.copy()


# In[16]:


print(citi_bike_df[['starttime', 'stoptime']].head(10))


# In[17]:


citi_bike_df['starttime'] = pd.to_datetime(citi_bike_df['starttime'], errors='coerce')
citi_bike_df['stoptime'] = pd.to_datetime(citi_bike_df['stoptime'], errors='coerce')

citi_bike_df.dtypes


# In[18]:


citi_bike_df.dtypes


# In[19]:


citi_bike_df.info()


# In[20]:


citi_bike_df


# In[21]:


citi_bike_df.copy()


# In[22]:


# Convert tripduration from seconds to a timedelta
citi_bike_df['tripduration_timedelta'] = pd.to_timedelta(citi_bike_df['tripduration'], unit='s')

# Display the DataFrame
citi_bike_df


# In[24]:


citi_bike_df.to_csv('citi_bike.csv')


# In[ ]:




