#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from collections import defaultdict
import ast


# In[2]:


dataDf = pd.read_csv('data/politics18.csv')


# In[20]:


dataDf.head()


# In[24]:


''' Not All Articles have Ministers Tagged In Them. Lets Populate a list of those who Do'''
import ast
ministerTaggedNewsArticlesIds = []
newsarticlesTag = []
for row in  dataDf.itertuples():
    if str(row[8])!='nan':
        ministerTaggedNewsArticlesIds.append(row[0])
        newsarticlesTag.append(ast.literal_eval(row[4]))


# In[26]:


ministerTaggedDf = dataDf[dataDf.index.isin(ministerTaggedNewsArticlesIds)]


# In[27]:


#ministerTaggedDf


# In[18]:


''' Now let's Populate a list of keywords for each minister in order of How well they are surrounded with that news'''

MinistersDf = pd.read_csv('data/ministers.csv')


# In[67]:


keywordsForMinister = defaultdict(list)
NewsIdsTagged = defaultdict(list)
for newsrow in ministerTaggedDf.itertuples():
    ministersTagged = newsrow[8].split(',')
    for minister in ministersTagged:
        keywordsForMinister[minister] = keywordsForMinister[minister] + ast.literal_eval(newsrow[4])
        NewsIdsTagged[minister].append(newsrow[0])
    
#Quick Fix. Lack of Time    


# In[71]:


for minister in MinistersDf['Name'].to_list():
    if minister not in keywordsForMinister.keys():
        keywordsForMinister[minister] = []
    if minister not in NewsIdsTagged.keys():
        NewsIdsTagged[minister] = []


# In[72]:


len(sorted(NewsIdsTagged.items()))


# In[73]:


keywordsForMinister =dict(sorted(keywordsForMinister.items()))
NewsIdsTagged =dict(sorted(NewsIdsTagged.items()))


# In[74]:


MinistersDf['taggedKeywords'] = keywordsForMinister.values()


# In[75]:


MinistersDf['taggedPages'] = NewsIdsTagged.values()


# In[76]:


MinistersDf


# In[78]:


MinistersDf.to_csv('data/ministers.csv', index= False)


# In[79]:


checkDf =  pd.read_csv('data/ministers.csv')


# In[81]:


checkDf.head()

