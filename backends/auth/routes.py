from backends import app


from .views import login, registration, logout


app.add_url_rule('/login', view_func=login, methods=['GET','POST'])
app.add_url_rule('/registration', view_func=registration, methods=['GET','POST'])
# app.add_url_rule('/registrationsuccessfull', view_func=registrationsuccessfull, methods=['GET','POST'])
app.add_url_rule('/logout', view_func=logout, methods=['GET','POST'])