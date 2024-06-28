#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[ ]:


#Load a CSV file into a Pandas DataFrame


# In[3]:


data=pd.read_csv("Diabetes Missing Data.csv")
data.head(10)


# In[ ]:


#operation like filtering data based on conditions


# In[8]:


data[data['Age']==50]


# In[10]:


data[data['BMI']==33.6]


# In[21]:


data[data['Diabetes_Pedigree'] != 0.510]


# In[28]:


a=data['Diastolic_BP']>72
data[a]


# In[30]:


data[data['Pregnant'] >= 6]


# In[31]:


data[data['Pregnant'] <= 6]


# In[32]:


#handling missing values
#isnull(),notnull(),dropna(),fillna()


# In[65]:


data.head()


# In[67]:


data.isnull().head()


# In[68]:


data.notnull().head()


# In[69]:


data.isnull().sum()


# In[71]:


data[data.Serum_Insulin.isnull()]


# In[72]:


data.shape


# In[73]:


data.dropna(how='any').shape


# In[74]:


data.dropna(how='all').shape


# In[75]:


data.dropna(subset='Diastolic_BP',how='all').shape


# In[77]:


data['Serum_Insulin'].fillna(value='VARIOUS',inplace=True)


# In[78]:


data['Serum_Insulin'].value_counts(dropna=False)


# In[33]:


#calculating summary statistics
#count(),value_counts(),min(),nsmallest(),max(),nlargest(),mean(),median(),mode(),std(),agg(),describe()


# In[38]:


#count()
data.count()


# In[40]:


data.count(axis=1)


# In[43]:


#value_counts()
data['Glucose'].value_counts(dropna=False,normalize=True)


# In[42]:


#min()
data['Diastolic_BP'].min()


# In[46]:


#nsmallest()
data['Diastolic_BP'].nsmallest(3,keep="all")


# In[45]:


#max()
data['Diastolic_BP'].max()


# In[47]:


#nlargest()
data['Diastolic_BP'].nlargest(3,keep="all")


# In[50]:


#mean()
data['Skin_Fold'].mean(axis=0)


# In[53]:


#median()
data[['Skin_Fold','Diastolic_BP']].median(axis=1)


# In[56]:


#mode()
data['Skin_Fold'].mode()


# In[59]:


#std()
data['Skin_Fold'].std()
data[['Skin_Fold','Diastolic_BP']].std(axis=0)


# In[60]:


#agg()
data.agg(["mean","median","std"])


# In[62]:


#describe()
data.describe(percentiles=[.2,.4,.6,.8])


# In[ ]:




