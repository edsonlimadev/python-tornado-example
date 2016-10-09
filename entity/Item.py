class Item(object):
	def __init__(self, key, name, type, status='Available'):
		self.key = key
		self.name = name
		self.type = type
		self.status = status

	def __str__(self):
		return '{0.type!s} - {0.name!s} ({0.status!s})'.format(self)