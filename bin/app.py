import web

urls = ('/hello', 'index')

app = web.application(urls, globals())

render = web.template.render('templates/', base='layout')

class index(object):
	def GET(self):
		return render.hello_form()
	def POST(self):
		form = web.input(name="World", greet="Hello")
		greeting = "%s, %s" % (form.greet, form.name)
		return render.index(greeting = greeting)

if __name__ == '__main__':
	app.run()