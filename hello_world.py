from pycnic.core import WSGI, Handler

class Hello(Handler):
	def get(self, message="Welcome to the Hello Handler!"):
		return { "message" : message }
	def post(self):
		return { "message" : "Thank you for your POST request!" }

class World(Handler):
	def get(self, message="Welcome to the World Handler!"):
		return { "message" : message }

class app(WSGI):
	routes = [
		("/", Hello()),
		("/a",World())
	]
