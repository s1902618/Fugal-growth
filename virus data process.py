#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.impute import SimpleImputer
import numpy as np


# In[2]:


virus_= pd.read_csv('enteric_virus.csv')


# In[3]:


virus = virus_.copy()


# In[4]:


virus = virus.loc[:, "Age": ]


# In[5]:


virus


# In[6]:


print(virus["BloodStool"].value_counts())
print(virus["MucoidStool"].value_counts())
print(virus["AbdominalPain"].value_counts())
print(virus["NumberDiarEpi"].value_counts())
print(virus["ThreeDaysFever"].value_counts())

print("Length of stay unique value counts:{}".format(len(virus["Length of stay"].unique())))
print(virus["Length of stay"].value_counts())

print("CentrallyCity unique value counts:{}".format(len(virus["CentrallyCity"].unique())))
print("ProvincialCity unique value counts:{}".format(len(virus["ProvincialCity"].unique())))
print(virus["CentrallyCity"].unique())
print(virus["ProvincialCity"].unique())
print("CentrallyCity value counts:{}".format(virus["CentrallyCity"].value_counts()))
print("ProvincialCity value counts:{}".format(virus["ProvincialCity"].value_counts()))

print("ContactDiar unique value counts:{}".format(len(virus["ContactDiar"].unique())))
print(virus["ContactDiar"].unique())
print(virus["ContactDiar"].value_counts())

print(virus["AbdominalPain"].value_counts())

print(virus["ThreeDaysFever"].value_counts())

print("NumberDiarEpi unique value counts:{}".format(len(virus["NumberDiarEpi"].unique())))
print(virus["NumberDiarEpi"].unique())
print(virus["NumberDiarEpi"].value_counts())
print(virus["NumberDiarEpi"].isna().sum())

print("HaemoglobinResult unique value counts:{}".format(len(virus["HaemoglobinResult"].unique())))
print(virus["HaemoglobinResult"].isna().sum())
print(virus["EosinophilsResult"].isna().sum())
print(virus["PlateletsResult"].isna().sum())

print("KnownTemp  unique value counts:{}".format(len(virus["KnownTemp"].unique())))
print(virus["KnownTemp"].unique())
print(virus["KnownTemp"].value_counts())
print(virus["KnownTemp"].isna().sum())


print("Temp unique value counts:{}".format(len(virus["Temp"].unique())))
print(virus["Temp"].isna().sum())

print(virus["Tap"].value_counts())
print(virus["Well"].value_counts())
print(virus["River"].value_counts())
print(virus["Pond"].value_counts())
print(virus["Bottled"].value_counts())
print(virus["OtherWS"].value_counts())

print(virus["KeepAnimal"].value_counts())
print(virus["KillingAnimal"].value_counts())
print(virus["EatCookRawMeat"].value_counts())
print(virus["Rotavirus.PCR."].value_counts())
print(virus["Norovirus2.PCR."].value_counts())
print(virus["Norovirus1.PCR."].value_counts())
print(virus["Aichivirus.PCR."].value_counts())
print(virus["Adenovirus.PCR."].value_counts())
print(virus["Sapovirus.PCR."].value_counts())
print(virus["Astrovirus.PCR."].value_counts())

viruses=['Rotavirus', 'Norovirus', 'Sapovirus', 'Kobuvirus','Mastadenovirus','Mamastrovirus','Alphapapillomavirus',
         'Alphapolyomavirus', 'Alphatorquevirus', 'Betapapillomavirus', 'Betapolyomavirus', 'Betatorquevirus', 'Bocaparvovirus',
         'Cardiovirus', 'Circovirus', 'Cosavirus', 'Cytomegalovirus', 'Enterovirus', 'Gammatorquevirus', 'Gemycircularvirus',
         'Gemykibivirus', 'Gemykrogvirus', 'Husavirus', 'Lymphocryptovirus', 'Morbillivirus', 'Parechovirus', 'Picobirnavirus',
         'Porprismacovirus', 'Protoparvovirus', 'Rubulavirus', 'Salivirus', 'Unclassified virus']
print(len(viruses))
for i in viruses:
    print(virus[i].value_counts())
    
    
print(virus["is_coinf"].value_counts())   
print(virus["is_coinf"].isna().sum())


# In[7]:


common_viruses=['Rotavirus', 'Norovirus', 'Sapovirus', 'Kobuvirus','Mastadenovirus','Mamastrovirus']

uncommon_viruses=['Alphapapillomavirus',
         'Alphapolyomavirus', 'Alphatorquevirus', 'Betapapillomavirus', 'Betapolyomavirus', 'Betatorquevirus', 'Bocaparvovirus',
         'Cardiovirus', 'Circovirus', 'Cosavirus', 'Cytomegalovirus', 'Enterovirus', 'Gammatorquevirus', 'Gemycircularvirus',
         'Gemykibivirus', 'Gemykrogvirus', 'Husavirus', 'Lymphocryptovirus', 'Morbillivirus', 'Parechovirus', 'Picobirnavirus',
         'Porprismacovirus', 'Protoparvovirus', 'Rubulavirus', 'Salivirus', 'Unclassified virus']


# In[8]:


for i in range(len(common_viruses)-1):
    for j in range(i+1,len(common_viruses)):
        f = common_viruses[i]
        l = common_viruses[j]
        virus[f+'_'+l]=virus[f]+virus[l]
        virus[f+'_'+l].replace([2,3,4],[1,0,0], inplace=True)


# In[ ]:





# In[9]:


virus.info()


# In[10]:


virus = virus.loc[:, (virus != 0).any(axis=0)]


# In[11]:


virus = virus[virus["BloodStool"]!=9]


# In[12]:


virus = virus[virus["MucoidStool"]!=9]


# In[13]:


virus = virus[virus["AbdominalPain"]!=9]


# In[14]:


virus = virus[virus["ThreeDaysFever"]!=9]


# In[15]:


# date object type change
virus["Date of hospital entry"] = pd.to_datetime(virus["Date of hospital entry"])
virus["AdminDate"] = pd.to_datetime(virus["AdminDate"])
virus["DateOnset"] = pd.to_datetime(virus["DateOnset"])
virus["DateDischOrDeath"] = pd.to_datetime(virus["DateDischOrDeath"])


# In[16]:


virus.BloodStool.replace(2, 0, inplace=True)
virus.MucoidStool.replace(2,0, inplace=True)
virus.ThreeDaysFever.replace(2,0, inplace=True)
virus.AbdominalPain.replace(2,0, inplace=True)


# In[17]:


imp=SimpleImputer(missing_values=np.nan, strategy='median' )
imp.fit(virus[['NumberDiarEpi']])
virus[['NumberDiarEpi']]=imp.transform(virus[['NumberDiarEpi']])


# In[18]:


#virus.AbdominalPain.replace([1,2],['Yes', 'No'], inplace=True)
#virus.ThreeDaysFever.replace([1,2],['Yes', 'No'], inplace=True)


# In[19]:


imp=SimpleImputer(missing_values=np.nan, strategy='median' )
imp.fit(virus[['HaemoglobinResult']])
virus[['HaemoglobinResult']]=imp.transform(virus[['HaemoglobinResult']])

imp.fit(virus[['WhiteCellsResult']])
virus[['WhiteCellsResult']]=imp.transform(virus[['WhiteCellsResult']])

imp.fit(virus[['NeutrophilsResult']])
virus[['NeutrophilsResult']]=imp.transform(virus[['NeutrophilsResult']])

imp.fit(virus[['LymphocytesResult']])
virus[['LymphocytesResult']]=imp.transform(virus[['LymphocytesResult']])

imp.fit(virus[['EosinophilsResult']])
virus[['EosinophilsResult']]=imp.transform(virus[['EosinophilsResult']])

imp.fit(virus[['PlateletsResult']])
virus[['PlateletsResult']]=imp.transform(virus[['PlateletsResult']])


# In[20]:


#virus["KnownTemp"] = virus["KnownTemp"].fillna(9)
#virus["KnownTemp"].replace([1,2,9],['Yes', 'No','NA'], inplace=True)


# In[21]:


virus.loc[ (virus.Temp.notnull()), 'Temp' ] = 1
virus.loc[ (virus.Temp.isnull()), 'Temp' ] = 0


# In[22]:


for i in viruses:
    virus[i].replace([1,2],['Yes', 'No'], inplace=True)
    


# In[23]:



#virus["is_coinf"] = virus["is_coinf"].fillna(0)
virus.dropna(subset = ["is_coinf"], inplace=True)
virus["is_coinf"] = virus["is_coinf"].mask(virus["is_coinf"] ==1, 0) 
virus["is_coinf"] = virus["is_coinf"].mask(virus["is_coinf"] >1, 1) 
#virus["is_coinf"].replace([1,2],['NO', 'YES'], inplace=True)
#dummies_is_coinf = pd.get_dummies(virus['is_coinf'], prefix= 'is_coinf')

#virus = pd.concat([virus, dummies_is_coinf], axis=1)
#virus.drop(['is_coinf'], axis=1, inplace=True)
virus


# In[24]:


virus.to_csv('virus_modified6.csv')


# In[58]:


virus.head()


# In[ ]:




