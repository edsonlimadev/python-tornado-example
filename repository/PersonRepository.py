import csv
from entity.Person import Person

class PersonRepository(object):
	def __init__(self, file):
		self.file = file

	def findAll(self):
		persons = []

		with open(self.file, 'rb') as csvfile:
			reader = csv.reader(csvfile, delimiter=',', quotechar='"')
			next(reader)
			for row in reader:
				persons += [Person(row[0], row[1])]

		return persons

	def findOneByEmail(self, email):
		persons = self.findAll()

		return reduce(self.filterByEmail(email), persons)

	def filterByEmail(self, email):
		def f(x, y):
			return x if x.email == email else y

		return f