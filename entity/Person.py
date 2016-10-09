class Person(object):
	def __init__(self, name, email):
		self.name = name
		self.email = email

	def __str__(self):
		return self.name
