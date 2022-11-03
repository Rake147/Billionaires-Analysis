#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[26]:


data=pd.read_csv('C:/Users/Rakesh/Datasets/Billionaire.csv')


# In[42]:


data.head(20)


# In[28]:


data.isnull().sum()


# In[29]:


data.shape


# In[30]:


data=data.dropna()


# In[31]:


data.shape


# In[32]:


data.dtypes


# In[33]:


data['NetWorth']=data['NetWorth'].str.strip('$')
data['NetWorth']=data['NetWorth'].str.strip('B')
data['NetWorth']=data['NetWorth'].astype(float)


# ## Will look at the top 10 Billionaires list

# In[34]:


df=data.sort_values(by=["NetWorth"], ascending=False).head(10)
plt.figure(figsize=(20,10))
sns.histplot(x='Name',hue="NetWorth",data=df)
plt.show()


# In[36]:


a=data["Source"].value_counts().head()
index=a.index
sources=a.values 
custom_colors=['skyblue','yellowgreen','tomato','blue','red']


# In[41]:


plt.figure(figsize=(5,5))
plt.pie(sources, labels=index, colors=custom_colors)
central_circle=plt.Circle((0,0), 0.5, color='white')
fig=plt.gcf()
fig.gca().add_artist(central_circle)
plt.rc('font', size=12)
plt.title('Top 5 Domains to Become a Billionaire', fontsize=20)
plt.show()


# In[44]:


a=data['Industry'].value_counts().head()
index=a.index
industries=a.values
custom_colors=['skyblue','yellowgreen','tomato','blue','red']
plt.figure(figsize=(5,5))
plt.pie(industries,labels=index, colors=custom_colors)
central_circle=plt.Circle((0,0),0.5,color='white')
fig=plt.gcf()
fig.gca().add_artist(central_circle)
plt.rc('font', size=12)
plt.title('Top 5 Industries with Most Number of Billionaires', fontsize=20)
plt.show()


# In[45]:


a=data['Country'].value_counts().head()
index=a.index
Countries=a.values
custom_colors=['skyblue','yellowgreen','tomato','blue','red']
plt.figure(figsize=(5,5))
plt.pie(Countries,labels=index, colors=custom_colors)
central_circle=plt.Circle((0,0),0.5,color='white')
fig=plt.gcf()
fig.gca().add_artist(central_circle)
plt.rc('font', size=12)
plt.title('Top 5 Countries with Most Number of Billionaires', fontsize=20)
plt.show()

