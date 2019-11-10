import pandas as pd
import ast

def viewNewsArticles(newsIDs,count = 50):
    df = pd.read_csv('data/politics18.csv')
    newsfeed = []
    renderedCount = 0
    matcheddf = df[df.index.isin(newsIDs)]
    for row in matcheddf.itertuples():
                    tagged = ast.literal_eval(row[4]) 
                    taggedMinisters = str(row[8]).split(',')
                    newsfeed.append({'author' : row[1],'content' : row[2],'date' : row[3],'tags' :tagged ,'title' : row[5],'url' : row[6],'website' : row[7],'taggedMinisters' :taggedMinisters })
                    renderedCount += 1
                    newsMatchedforTopic = 1
                    if newsMatchedforTopic >=count:
                        break
    return newsfeed

def returnDetails(ministerName):
    df =  pd.read_csv('data/ministers.csv')
    row = df.loc[df['Name'] == ministerName]
    name = ministerName
    party = row['Party'].to_list()[0]
    portfolio =  row['Portfolio'].to_list()[0] #Fix Portfolio Later
    terms = list(set(ast.literal_eval(row['taggedKeywords'].to_list()[0])))
    newsIDs = ast.literal_eval(row['taggedPages'].to_list()[0])
    
    details = {'name' : name,'party': party,
               'portfolio' : portfolio, 
               'terms' : terms,
               'newsfeed' : viewNewsArticles(newsIDs)}
    
    #Fix Portfolio Later
    return details