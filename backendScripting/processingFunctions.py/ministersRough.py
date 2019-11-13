'''Just storing how i got the data processed. Reusable onlu by author. Not really neat'''

import pandas as pd
import operator,csv
from collections import Counter,defaultdict


'''View the ministers we have'''
def viewministers():
    with open('data/ministers.csv', 'r') as f: #Was old file
        reader = csv.reader(f)
        your_list = list(reader)
    return [keyword[1].lower() for keyword in your_list]

ministers = viewministers()

'''We are going to analyse the news for how the ministers are tagged'''

df = pd.read_csv('data/politics18.csv')

from collections import defaultdict
ministerCountList = []
ministerTaggedDocs = defaultdict(list)
for items in df.itertuples():
    news = items[2].lower()
    countdict = defaultdict(dict)
    for minister in ministers:
        if minister in news:
            countdict[minister]=news.count(minister)
            ministerTaggedDocs[minister].append(int(items[0]))
    ministerCountList.append(countdict)        
    
keywordsInNewsList = [str(row[4]).split(',') for row in df.itertuples()]


keywordsAssociated =defaultdict(list)
for minister in ministers:
    tags =[]
    for news in ministerTaggedDocs[minister]:
        tags.extend(keywordsInNewsList[news])
    topKeywords = dict(Counter(tags))
    keywordsAssociated[minister]= sorted(topKeywords.items(), key=operator.itemgetter(1), reverse=True)
    
'''Storing the info into csv'''
taggedDocs =[ministerTaggedDocs[minister] for minister in ministers]


df = pd.read_csv('data/ministers.csv',names=['Name','Party','Portfolio'])
df['taggedKeywords'] = dict(keywordsAssociated).values()
df['taggedPages']=taggedDocs

#df.to_csv("data/ministers.csv")