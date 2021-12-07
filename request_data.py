from pycnic.core import Handler, WSGI

class ReqData(Handler):
	def post(self):
		return { 
		"request_data" : self.request.data,
		"ip" : self.request.ip,
		"method" : self.request.method,
		"args" : self.request.args,
		"json_args" : self.request.json_args,
		"header" : self.request.get_header("X-Forwarded-For"),
		"a" : self.request.data["a"]
	}

class app(WSGI):
	routes = [
		("/",ReqData())
	]
