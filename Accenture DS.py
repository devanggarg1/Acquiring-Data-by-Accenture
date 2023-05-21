#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np


# In[7]:


#creating list of lists

data =[["Alex","Mumbai",23,88.0],["Ben","Chennai",25,89.0],["David","New Delhi",33,83.0]]

#creating pandas Data Frame

df=pd.DataFrame(data,columns=['Name','City','Age','Percent'])

#print Data Frame

df


# In[8]:


data={
    'Name':['Alex','Ben','David','Eva'],
    'City':['Mumbai','Chennai','New Delhi','Kolkata'],
    'Age':[23,23,33,34],
    'Percent':[88.0,89.0,83.0,80.0]
}

df=pd.DataFrame(data)

df


# In[11]:


#3 Dictionary of numPy Arrays

nparray=np.array([['Alex','Ben','David','Eva'],['Mumbai','Chennai','New Delhi','Kolkata'],[23,25,33,34],[880,89.0,83.0,80.0]])

data={'Name': nparray[0],
     'City': nparray[1],
      'Age': nparray[2],
      'Percent': nparray[3]
     }

df=pd.DataFrame(data)
df


# In[12]:


#4 list of dictionaries

data =[{'Name':'Alex','City':'Mumbai','Age':23,'Percent':88.0},
      {'Name':'Ben','City':'Delhi','Age':22,'Percent':89.0},
       {'Name':'David','City':'Kolkata','Age':27,'Percent':85.9},
      {'Name':'Eva','City':'jaipur','Age':24,'Percent':83.0},
      ]
df=pd.DataFrame(data)
df


# In[13]:


#4.1 List of Dictionaries with indexes

data =[{'Name':'Alex','City':'Mumbai','Age':23,'Percent':88.0},
      {'Name':'Ben','City':'Delhi','Age':22,'Percent':89.0},
       {'Name':'David','City':'Kolkata','Age':27,'Percent':85.9},
      {'Name':'Eva','City':'jaipur','Age':24,'Percent':83.0},
      ]
df=pd.DataFrame(data,index=['first','second','third','fourth'])

df


# In[14]:


#dictionaris of seies

data={'Name':pd.Series(['Alex','Ben','David','Eva'],index=['p','q','r','s']),
     'City':pd.Series(['Mumbai','Chennai','Delhi','Jaipur'],index=['p','q','r','s']),
      'Age':pd.Series([23,25,32,21],index=['p','q','r','s']),
      'Percent':pd.Series([82.10,83.00,91.00,89.05],index=['p','q','r','s'])
     }

df=pd.DataFrame(data)
df


# In[16]:


# 6 Data Frame from CSV file

df=pd.read_csv('winequality-white.csv',sep=';',header='infer',index_col=None)

df.head()


# In[17]:


df=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv',sep=';')

df.head()


# In[19]:


data =[["Alex","Team1",251,242,39,12040,183,59.31,43,60],
       ["Henry","Team2",77,79,39,12040,183,59.31,43,60],
       ["Alex","Team1",251,242,39,12040,183,59.31,43,60],
       ["Alex","Team1",251,242,39,12040,183,59.31,43,60],
       ["Alex","Team1",251,242,39,12040,183,59.31,43,60],
       ["Alex","Team1",251,242,39,12040,183,59.31,43,60],
       ["Alex","Team1",251,242,39,12040,183,59.31,43,60],
       ["Alex","Team1",251,242,39,12040,183,59.31,43,60]
      ]

#creating pandas Data Frame

df=pd.DataFrame(data,columns=['Player','Team','Matches','Innings','NO','RUns','HS',"Average",'100s','50s'])

#print Data Frame

df


# In[21]:


df=pd.read_csv('diabetes_data_upload.csv',sep=';',header='infer',index_col=None)

df.head()


# In[22]:


df=pd.read_csv('iris.data')
df.columns


# In[23]:


df.axes


# In[24]:


df.ndim


# In[26]:


df.info()


# In[27]:


df.describe()


# In[28]:


df=pd.read_csv('country_vaccinations.csv')
df.columns


# In[29]:


df.axes


# In[30]:


df.ndim


# In[32]:


df.info()


# In[34]:


df.describe()


# In[35]:


df.head()


# In[36]:


df=pd.read_csv('country_vaccinations_by_manufacturer.csv')
df.columns


# In[37]:


df.axes


# In[38]:


df.ndim


# In[39]:


df.describe


# In[2]:


import pandas as pd
df1=pd.read_csv("covid_19_india.csv")
df1.head()


# In[3]:


df1.shape


# In[4]:


df2=pd.read_csv("covid_19_india.csv",index_col=0)
df2.head()


# In[5]:


df4=pd.read_csv("covid_19_india.csv",header=None)
df4.head()


# In[6]:


df5=pd.read_csv("covid_19_india.csv",header=None,prefix='India')
df5.head()


# In[7]:


df6=pd.read_csv("covid_19_india.csv",header=2)
df6.head()


# In[8]:


df6.columns()


# In[13]:


df8=pd.read_csv("covid_19_india.csv",nrows=10,header=None)
df8.head()


# In[14]:


df8.shape


# In[15]:


df1=pd.read_csv("netflix_titles.csv")
df1.head()


# In[16]:


df1.shape


# In[17]:


df1.isnull().sum()


# In[18]:


df1.dropna(inplace=True)


# In[19]:


df1.isnull().sum()


# In[21]:


df1.info()


# In[22]:


df1.head()


# In[25]:


df1=pd.read_csv("netflix_titles.csv",parse_dates=['date_added'])


# In[26]:


df1.head()


# In[27]:


df1.info()


# In[28]:


df1=pd.read_csv("netflix_titles.csv",nrows=1000,header=None)


# In[29]:


df1.head()


# In[30]:


df1.shape


# In[31]:


df1=pd.read_csv("netflix_titles.csv",index_col=0,usecols=['show_id','type','country','date_added','release_year','description'])
df1.head()


# In[ ]:




