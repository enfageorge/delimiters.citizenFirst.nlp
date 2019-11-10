import pandas as pd
import ast
def returnDetails(ministerName):
    #ministerName = 'Narendra Modi'
    row = checkDf.loc[df['Name'] == ministerName]
    name = ministerName
    party = row['Party'].to_list()[0]
    portfolio =  row['Portfolio'].to_list()[0] #Fix Portfolio Later
    terms = list(set(ast.literal_eval(row['taggedKeywords'].to_list()[0])))
    newsIDs = ast.literal_eval(row['taggedPages'].to_list()[0])
    
    details = {'name' : name,'party': party,
               'portfolio' : portfolio, 
               'terms' : terms,
               'newsIDs' : newsIDs}
    
    #Fix Portfolio Later
    return details