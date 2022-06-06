from backends import app
from .views import dashboard


app.add_url_rule('/', view_func=dashboard, methods=['GET','POST'])


