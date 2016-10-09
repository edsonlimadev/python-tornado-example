from repository.ItemRepository import ItemRepository
import tornado.web

class ItemsHandler(tornado.web.RequestHandler):
	def get(self):
		repository = ItemRepository('data/items.csv')
		self.render('../view/html/items.html', title='Items', items=repository.findAll())