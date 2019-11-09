import csv, ast

class User(object):
	"""userName is assumed to be a unique identifier for each user. Can be improved later with numeric IDs
	userCauses is a list of strings that contains the causes the user identifies with. Limited to just 5 ideally

	Further modifications include editing topics, deleting users etc """
	def __init__(self, name,causes):
		super(User, self).__init__()
		self.userName = name
		self.userCauses = causes

		""" Adding user details to a file"""


		with open("users.csv", "a", newline='') as fp:
			wr = csv.writer(fp)
			wr.writerow((self.userName, self.userCauses))



def userViewTopics(userName):
	''' Returns the topics the user aligns care about'''
	
	rows = csv.reader(open('users.csv', 'r'))
	for row in rows:
		if userName in row:
			return ast.literal_eval(row[1])


		