from pycnic.core import Handler, WSGI
from pycnic.errors import HTTPError
from pycnic.utils import requires_validation


class ValidationError(HTTPError):
	status_code = 400
	message = "Invalid data recieved from client!"
	def __init__(self):
		...
	def response(self):
		return {
			"error" : self.message,
			"data" : {"required":"name"},
			"status_code" : self.status_code,
			"status" : "400 Validation Error"
		}


def has_proper_data(data):
        if not data.get('name'):
                raise ValidationError()

class BeforeRequest(Handler):
	def before(self):
		if 'name' not in self.request.data:
			raise ValidationError()
	def post(self):
		return {"status":"ok"}

class DecoratorBased(Handler):
	@requires_validation(has_proper_data)
	def post(self):
		return {"status_decorator_based":"ok"}


class app(WSGI):
	routes = [("/before",BeforeRequest()),("/decorator",DecoratorBased())]