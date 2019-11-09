import pandas as pd
from collections import defaultdict

newsDf = pd.read_csv('data/politics18.csv')

ministersDf = pd.read_csv('data/ministers.csv')


ministersInNews = defaultdict(str)
for content in newsDf['content'].to_list():
    taggedMinisters = []
    for minister in ministersDf['Name'].to_list():
        if minister.lower() in content.lower():
            taggedMinisters.append(minister)
    ministersInNews[content] =','.join(taggedMinisters)     
    
taggedMinisters = ministersInNews.values()

newsDf['taggedMinisters'] = taggedMinisters

newsDf.to_csv('data/politics18.csv',index=False)