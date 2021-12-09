from functools import wraps
from pycnic.errors import HTTP_401
from pycnic.core import WSGI, Handler

def get_user_role(request):
	return "admin"

def requires_roles(*args):
	def wrapper(f):
		@wraps(f)
		def wrapped(*args, **kwargs):
			if get_user_role(args[0].request) not in ["admin","user"]:
				raise HTTP_401("You shall not pass!")
			return f(*args, **kwargs)
		return wrapped
	return wrapper

class AuthDemo(Handler):
	@requires_roles("admin")
	def get(self):
		return {"welcome" : "administrator"}

class app(WSGI):
	routes = [("/",AuthDemo())]
