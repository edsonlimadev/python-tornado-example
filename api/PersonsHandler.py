from repository.PersonRepository import PersonRepository
import tornado.web

class PersonsHandler(tornado.web.RequestHandler):
	def get(self):
		repository = PersonRepository('data/persons.csv')
		self.render('../view/html/persons.html', title='Persons', persons=repository.findAll())