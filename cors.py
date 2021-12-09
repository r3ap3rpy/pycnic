from pycnic.core import WSGI, Handler

class CorsTester(Handler):
	def get(self):
		return { 
			"message" : "CORS is working!",
			"origin":self.request.get_header("Origin")
		}
	def options(self):
		return {
			"GET" : {
				"description" : "Test cross site origin",
				"parameters" : None
			}
		}

class app(WSGI):
	routes = [("/",CorsTester())]
