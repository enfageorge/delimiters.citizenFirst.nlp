import pandas as pd
import ast
def viewNewsArticles(topicArray,count = 50):
    df = pd.read_csv('data/politics18.csv')
    newsfeed = []
    renderedCount = 0
    for row in df.itertuples():
        newsMatchedforTopic = 0
        for topic in topicArray:
            if (newsMatchedforTopic == 0):
                tagged = ast.literal_eval(row[4])    
                if topic in tagged:
                    newsfeed.append({'author' : row[1],'content' : row[2],'date' : row[3],'tags' : tagged,'title' : row[5],'url' : row[6],'website' : row[7],'taggedMinisters' : str(row[8]).split(',')})
                    renderedCount += 1
                    newsMatchedforTopic = 1
            else:
                break
            if newsMatchedforTopic >=count:
                break
    return newsfeed
