from repository.PersonRepository import PersonRepository
import tornado.web

class PersonHandler(tornado.web.RequestHandler):
	def get(self, email):
		repository = PersonRepository('data/persons.csv')
		self.render('../view/html/person.html', title='Person', person=repository.findOneByEmail(email))