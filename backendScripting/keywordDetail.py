import csv

def viewKeywords():
	with open('data/causekeywords.csv', 'r') as f:
	    reader = csv.reader(f)
	    your_list = list(reader)
	return [keyword[0] for keyword in your_list][1:]
