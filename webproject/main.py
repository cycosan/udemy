import web
url=('/(.*)/(.*)','index')
render=web.template.render("resources/")
app=web.application(url,globals())
class index:
    def GET(self,name,age):
        return render.main(name,age)
if __name__=="__main__":
    app.run()