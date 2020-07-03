#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
get_ipython().system('{sys.executable} -m pip install folium')


# In[2]:


import sys
get_ipython().system('{sys.executable} -m pip install plotly.express')


# In[41]:


import pandas as pd
import folium
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.offline as py


# In[42]:


virus = pd.read_csv('enteric_virus.csv')
virus.loc[:,'Alphapapillomavirus':'Unclassified virus']


# In[19]:


map = folium.Map(location=[10.47068691,105.6360626], zoom_start=0.001,tiles='Stamen Toner')

for lat, lon,CentrallyCity, ProvincialCity in zip(virus['LATITUDE'], virus['LONGITUDE'],virus['CentrallyCity'],virus['ProvincialCity']):
    folium.CircleMarker([lat, lon],
                        color='red',
                 
                 popup =('CentrallyCity: ' + str(CentrallyCity) + '<br>'
                        'ProvincialCity : ' + str(ProvincialCity) + '<br>'),

                        fill_color='red',
                        fill_opacity=0.1 ).add_to(map)
map


# In[20]:


fig = px.pie( values=virus.groupby(['ProvincialCity']).size().values,names=virus.groupby(['ProvincialCity']).size().index)
fig.update_layout(
    font=dict(
        size=15,
        color="#242323"
    )
    )   
    
py.iplot(fig)


# In[43]:


Common_Viruses = ['Rotavirus', 'Norovirus', 'Sapovirus', 'Kobuvirus','Mastadenovirus','Mamastrovirus']

virus_common = virus.copy()

for i in virus_common.loc[:,'Alphapapillomavirus':'Unclassified virus']:
    if i not in Common_Viruses:
        virus_common = virus_common.drop([i],axis=1)

        
virus_common = virus_common [~( virus_common [ Common_Viruses] == 2).all(axis=1) ]


# In[33]:



Uncommon_viruses=['Alphapapillomavirus',
         'Alphapolyomavirus', 'Alphatorquevirus', 'Betapapillomavirus', 'Betapolyomavirus', 'Betatorquevirus', 'Bocaparvovirus',
         'Cardiovirus', 'Circovirus', 'Cosavirus', 'Cytomegalovirus', 'Enterovirus', 'Gammatorquevirus', 'Gemycircularvirus',
         'Gemykibivirus', 'Gemykrogvirus', 'Husavirus', 'Lymphocryptovirus', 'Morbillivirus', 'Parechovirus', 'Picobirnavirus',
         'Porprismacovirus', 'Protoparvovirus', 'Rubulavirus', 'Salivirus', 'Unclassified virus']



virus_common = virus.copy()

for i in virus_common.loc[:,'Alphapapillomavirus':'Unclassified virus']:
    if i not in Uncommon_viruses:
        virus_common = virus_common.drop([i],axis=1)

        
virus_common = virus_common [~( virus_common [ Uncommon_viruses] == 2).all(axis=1) ]


# In[34]:


fig = px.pie( values=virus_common.groupby(['CentrallyCity']).size().values,names=virus_common.groupby(['CentrallyCity']).size().index)
fig.update_layout(
    font=dict(
        size=15,
        color="#242323"
    )
    )   
    
py.iplot(fig)


# In[36]:


fig = px.pie( values=virus_common.groupby(['ProvincialCity']).size().values,names=virus_common.groupby(['ProvincialCity']).size().index)
fig.update_layout(
    font=dict(
        size=15,
        color="#242323"
    )
    )   
    
py.iplot(fig)


# In[46]:


import seaborn as sns
from matplotlib import pyplot

fig, axs = plt.subplots(2,3, figsize=(15,15))
for v ,se in zip(Common_Viruses,range(1,7)):
    re_query = '{} == "1"'.format(v)
    a = virus_common.groupby(['ProvincialCity', v]).count().query(re_query)
    a = a.reset_index(level=['ProvincialCity', v])

    dic={}
    for i ,j in zip(a['ProvincialCity'],a['Sample ID']):
        dic[i] = j

    names = list(dic.keys())
    values = list(dic.values())
    
    # Visualization

    plt.subplot(2, 3, se)
    plt.bar(range(len(dic)),values,tick_label=names)
    plt.xticks(rotation=90)
    plt.title(v)

    plt.ylabel('# patients with common viruses')

plt.show()


# In[31]:


plt.figure(figsize=(15,5))
plt.title('Number of  patients in province')
virus_common.ProvincialCity.value_counts().plot.bar()


# In[64]:


Common_Viruses = ['Rotavirus', 'Norovirus', 'Sapovirus', 'Kobuvirus','Mastadenovirus','Mamastrovirus']
Uncommon_Viruses =[]
virus_uncommon = virus.copy()

for i in virus_uncommon.loc[:,'Alphapapillomavirus':'Unclassified virus']:
    if i in Common_Viruses:
        Uncommon_Viruses = Uncommon_Viruses
        virus_uncommon = virus_uncommon.drop([i],axis=1)
    else:
        Uncommon_Viruses.append(i)
print(Uncommon_Viruses)
virus_uncommon = virus_uncommon [~( virus_uncommon [Uncommon_Viruses] == 2).all(axis=1) ]


# In[53]:


import seaborn as sns
from matplotlib import pyplot

fig, axs = plt.subplots(5,3, figsize=(15,15))
for i ,se in zip(Uncommon_Viruses,range(1,16)):
    re_query = '{} == "1"'.format(i)
    a = virus_uncommon.groupby(['ProvincialCity', i]).count().query(re_query)
    a = a.reset_index(level=['ProvincialCity', i])

    dic={}
    for i ,j in zip(a['ProvincialCity'],a['Sample ID']):
        dic[i] = j
    print(dic)
    names = list(dic.keys())
    values = list(dic.values())
    
    # Visualization

    plt.subplot(5, 3, se)
    plt.bar(range(len(dic)),values,tick_label=names)
    plt.xticks(rotation=90)

        
    
plt.show()


# In[63]:


map = folium.Map(location=[10.47068691,105.6360626], zoom_start=0.001,tiles='Stamen Toner')

for lat1, lon1,CentrallyCity1, ProvincialCity1,lat2, lon2,CentrallyCity2, ProvincialCity2 in zip(virus_common['LATITUDE'], virus_common['LONGITUDE'],
                                                      virus_common['CentrallyCity'],virus_common['ProvincialCity'],
                                                     virus_uncommon['LATITUDE'], virus_uncommon['LONGITUDE'],
                                                     virus_uncommon['CentrallyCity'],virus_uncommon['ProvincialCity']):
    folium.CircleMarker([lat1, lon1],
                        color='red',
                 
                 popup =('CentrallyCity: ' + str(CentrallyCity1) + '<br>'
                        'ProvincialCity : ' + str(ProvincialCity1) + '<br>'),

                        fill_color='red',
                        fill_opacity=0.7 ).add_to(map)
    folium.CircleMarker([lat2, lon2],
                        color='green',
                 
                 popup =('CentrallyCity: ' + str(CentrallyCity2) + '<br>'
                        'ProvincialCity : ' + str(ProvincialCity2) + '<br>'),

                        fill_color='red',
                        fill_opacity=0.7 ).add_to(map)
    
map


# In[ ]:




