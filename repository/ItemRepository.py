import csv
from entity.Item import Item

class ItemRepository(object):
	def __init__(self, file):
		self.file = file

	def findAll(self):
		items = []

		with open(self.file, 'rb') as csvfile:
			reader = csv.reader(csvfile, delimiter=',', quotechar='"')
			next(reader)
			for row in reader:
				items += [Item(row[0], row[1], row[2], row[3].strip() if row[3].strip() else 'Available')]

		return items