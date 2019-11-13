#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import ast
from collections import Counter, defaultdict


# In[8]:


df = pd.read_csv('data/ministers.csv')
df.head()


# In[29]:


ministers = defaultdict(dict)
for row in df.itertuples():
    ministers[row[1]] = dict(Counter(ast.literal_eval(row[4])))


# In[30]:


ministers


# In[47]:


import csv,operator

def viewKeywords():
	with open('data/causekeywords.csv', 'r') as f:
	    reader = csv.reader(f)
	    your_list = list(reader)
	return [keyword[0] for keyword in your_list][1:]

keywords = viewKeywords()


# In[57]:


causeRank = defaultdict(dict)
for keyword in keywords:
    tempdict = defaultdict(int)
    for minister in ministers.items():
        if keyword in minister[1].keys():
            tempdict[minister[0]] = minister[1][keyword]
    causeRank[keyword] = dict(sorted(tempdict.items(), key=operator.itemgetter(1), reverse = True))


# In[64]:


topics = causeRank.keys()
len(topics)


# In[79]:


rankedministers= []
for topic in list(causeRank.keys()):
    rankedministers.append(list(causeRank[topic].keys()))


# In[83]:


pd.DataFrame({'topics':list(causeRank.keys()),'ministers': rankedministers }).to_csv('data/Ranked List.csv', index = False)


# In[101]:


topic = 'Terrorism'
def returnRank(topic):
    df =pd.read_csv('data/Ranked List.csv')
    return ast.literal_eval(((df.loc[df['topics'] == topic]['ministers']).to_dict()[1]))


# In[102]:


returnRank(topic)


# In[100]:


ast.literal_eval(((df.loc[df['topics'] == topic]['ministers']).to_dict()[1]))


# In[99]:


return ast.literal_eval(tempString)


# In[ ]:




