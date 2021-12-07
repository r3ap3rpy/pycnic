from pycnic.core import WSGI, Handler


class CookieMonster(Handler):
	def get(self):
		return { "gift" : self.request.cookies }

	def post(self):
		self.response.set_cookie("My Cookie Key","My Cookie Value", domain = "My Custom Domain")
		return {"Cookie":"was set!"}

class app(WSGI):
	routes = [("/",CookieMonster())]
