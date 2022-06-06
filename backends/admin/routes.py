from backends import app

from .views import adminpage, status


app.add_url_rule('/adminpage', view_func=adminpage, methods=['GET','POST'])
app.add_url_rule('/status', view_func=status, methods=['GET','POST'])