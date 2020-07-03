#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.impute import SimpleImputer
import numpy as np


# In[2]:


virus = pd.read_csv('enteric_virus.csv')


# In[3]:


virus.columns


# In[4]:


virus["is_coinf"] = virus["is_coinf"].fillna(0)

usful = ['Age','Year of enrollment','Gender','DOB_Year',
        'ContactDiar','Tap',"Well","Rain","River","Pond","Bottled","KeepAnimal","KillingAnimal","EatCookRawMeat",'is_coinf']

usful2 = ['Year of enrollment','Gender',
        'ContactDiar','Tap',"Well","Rain","River","Pond","Bottled","KeepAnimal","KillingAnimal","EatCookRawMeat",'is_coinf']

df = [virus[i] for i in virus if i in usful]
df = pd.DataFrame(df)
X= df.T 


for i in usful2:
    X[i] = X[i].astype("object")
X["Age"] = X["Age"].astype("int16")
X["DOB_Year"] =X["DOB_Year"].astype("int16")
X["is_coinf"] =X["is_coinf"].astype("int16")


y =  virus['is_coinf']

X.info()


# In[5]:



# sklearn preprocessing for dealing with categorical variables
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
le_count = 0

# Iterate through the columns
for col in X:
    if X[col].dtype == 'object':
        # If 2 or fewer unique categories
        if len(list(X[col].unique())) <= 2:
            # Train on the training data
            le.fit(X[col])
            # Transform both training and testing data
            X[col] = le.transform(X[col])
            
            # Keep track of how many columns were label encoded
            le_count += 1
            
print('%d columns were label encoded.' % le_count)


# In[6]:


X = pd.get_dummies(X)
print('Training Features shape: ', X.shape)


# In[7]:


X.corr(method='spearman')


# In[8]:


# Find correlations with the target and sort
correlations = X.corr(method='spearman')['is_coinf'].sort_values()

# Display correlations
print('Most Positive Correlations:\n', correlations.tail(15))
print('\nMost Negative Correlations:\n', correlations.head(15))


# In[9]:


correlations = X.corr(method='spearman')
correlations


# In[10]:


import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize = (8, 6))

# Heatmap of correlations
sns.heatmap(correlations, cmap = plt.cm.RdYlBu_r)
plt.title('Correlation Heatmap');


# In[11]:


X["is_coinf"] = X["is_coinf"].mask(X["is_coinf"] >2, 3) 


# In[12]:


plt.figure(figsize = (10, 8))

# KDE plot of loans that were repaid on time
plt.hist(virus.loc[virus['is_coinf'] == 0, 'EatCookRawMeat'] , label = 'is_coinf == 0')

# KDE plot of loans which were not repaid on time
plt.hist(virus.loc[virus['is_coinf'] == 1, 'EatCookRawMeat'], label = 'is_coinf == 1')

# KDE plot of loans which were not repaid on time
plt.hist(virus.loc[virus['is_coinf'] == 2, 'EatCookRawMeat'], label = 'is_coinf == 2')

# KDE plot of loans which were not repaid on time
plt.hist(virus.loc[virus['is_coinf'] == 3, 'EatCookRawMeat'], label = 'is_coinf == 3')

# Labeling of plot
plt.xlabel('Age (years)'); plt.ylabel('Density'); plt.title('Distribution of Ages');

