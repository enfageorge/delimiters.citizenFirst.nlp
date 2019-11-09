import pandas as pd
def viewNewsArticles(topicArray,count = 50):
    df = pd.read_csv('data/politics18.csv')
    newsfeed = {}
    renderedCount = 0
    for row in df.itertuples():
        newsMatchedforTopic = 0
        for topic in topicArray:
            if (newsMatchedforTopic == 0):
                if topic in str(row[4]).split(','):
                    #print(row[0])
                    newsfeed[int(row[0])] = {'author' : row[1],'content' : row[2],'date' : row[3],'tags' : str(row[4]).split(','),'title' : row[5],'url' : row[6],'website' : row[7],'taggedMinisters' : str(row[8]).split(' ')}
                    renderedCount += 1
                    newsMatchedforTopic = 1
            else:
                break
            if newsMatchedforTopic >=count:
                break
    return newsfeed