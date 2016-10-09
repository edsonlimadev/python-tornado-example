from api.ItemsHandler import ItemsHandler
from api.PersonsHandler import PersonsHandler
from api.PersonHandler import PersonHandler
import tornado.ioloop
import tornado.web

def make_app():
    return tornado.web.Application([
        (r"/items", ItemsHandler),
        (r"/persons", PersonsHandler),
        (r"/persons/(.*)", PersonHandler),
    ])

if __name__ == '__main__':
	app = make_app()
	app.listen(8888)
	tornado.ioloop.IOLoop.current().start()