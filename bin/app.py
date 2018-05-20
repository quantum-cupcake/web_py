import web

urls = ('/hello', 'index')

app = web.application(urls, globals())

render = web.template.render('templates/', base='layout')

class index(object):
	def GET(self):
		return render.hello_form()
	def POST(self):
		form = web.input(name="World", greet="Hello", myfile={})
		greeting = "%s, %s" % (form.greet, form.name)
		filename = form['myfile'].filename
		if filename and filename.split('.')[-1] in ['jpg', 'jpeg', 'png', 'gif']:
			with open('./static/'+filename, 'wb') as f:
				f.write(form.myfile.value)
			return render.index(greeting = greeting, filename = filename)
		else:
			return render.index(greeting = greeting)

if __name__ == '__main__':
	app.run()