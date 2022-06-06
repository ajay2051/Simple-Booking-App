from backends import app
from .views import (
            day, 
            admin,
            timeslot, 
            alladmins, 
            updateadmin, 
            deleteadmin, 
            alldays,
            deleteday,
            allslots,
            deleteslots,
            bookappointment
            # ,datetimeslot
            )



#Admins
app.add_url_rule('/admin', view_func=admin, methods=['GET','POST'])
app.add_url_rule('/alladmins', view_func=alladmins, methods=['GET','POST'])
app.add_url_rule('/updateadmin/<int:id>', view_func=updateadmin, methods=['GET','POST'])
app.add_url_rule('/deleteadmin/<int:id>', view_func=deleteadmin, methods=['GET','POST'])


#Days
app.add_url_rule('/day', view_func=day, methods=['GET','POST'])
app.add_url_rule('/alldays', view_func=alldays, methods=['GET','POST'])
app.add_url_rule('/deleteday/<int:id>', view_func=deleteday, methods=['GET','POST'])


#Time Slot
app.add_url_rule('/timeslot', view_func=timeslot, methods=['GET','POST'])
app.add_url_rule('/allslots', view_func=allslots, methods=['GET','POST'])
app.add_url_rule('/deleteslots/<int:id>', view_func=deleteslots, methods=['GET','POST'])


#bookappointment
app.add_url_rule('/bookappointment', view_func=bookappointment, methods=['POST','GET'])
# app.add_url_rule('/bookappointment/date?=2022-05-01', view_func=bookappointment, methods=['GET'])


# app.add_url_rule('/datetimeslot', view_func=datetimeslot, methods=['GET'] )