from pycnic.core import WSGI, Handler
from pycnic.errors import HTTPError

class MyError(HTTPError):
	status_code = 469
	message = "This is my own custom error class!"
	def __init__(self):
		pass
	def response(self):
		return {
			"error" : self.message,
			"data" : {"my_error_key" : "my_error_value"},
			"status_code" : self.status_code,
			"status" : "469 Custom Error"
		}

class CustErr(Handler):
	def get(self):
		raise MyError()

class app(WSGI):
	routes = [("/",CustErr())]
