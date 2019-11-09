import pandas as pd



def returnDetails(ministerName):
    df = pd.read_csv('data/ministers.py')
    row = df.loc[df['Name'] == ministerName]
    name = ministerName
    party = row['Party'].to_list()[0]
    portfolio =  row['Portfolio'].to_list() 
    tuplelist = row['taggedKeywords']
    termsWithSpaces = [re.sub(r"[^a-zA-Z0:9]+", ' ',item) for item in tuplelist.to_list()[0].split(',')]
    terms = [term for term in termsWithSpaces if term !=' ']
    newsIDs= row['taggedPages'].to_list()[0].strip('][').split(', ') 

    return name,party,portfolio,terms[0:10],newsIDs
