from pycnic.core import WSGI, Handler
from pycnic.errors import HTTP_400

class Error(Handler):
	def get(self):
		raise HTTP_400("Well this is not working!")


class app(WSGI):
	routes = [
		("/",Error())
	]
