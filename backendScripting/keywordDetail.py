import csv

def viewKeywords():
	with open('data/causekeywords.csv', 'r') as f:
	    reader = csv.reader(f)
	    your_list = list(reader)
	return [keyword[] for keyword in your_list][1:]
