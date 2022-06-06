from flask_wtf import FlaskForm
from wtforms import validators
from .models import Admin, Time
from wtforms.validators import DataRequired
from wtforms import (
        StringField, 
        PasswordField, 
        EmailField, 
        SubmitField, 
        RadioField, 
        DateField,
        TextAreaField,
        SelectField)


class DayForm(FlaskForm):
    add_day = StringField('Add Day', validators=[DataRequired()])
    time_slot = StringField('Add Time Slot', validators=[DataRequired()])
    add = SubmitField('Add')


# class TimeSlot(FlaskForm):
#     time_slot = StringField('Add Time Slot', validators=[DataRequired()])
#     add = SubmitField('Add')



class AdminForm(FlaskForm):
    admin = StringField('Add Admin', validators=[DataRequired()])
    add = SubmitField('Add')


class AdminUpdateForm(FlaskForm):
    admin = StringField('Add Admin', validators=[DataRequired()])
    update = SubmitField('Update')


class BookAppointment(FlaskForm):
    alltimeslots = Time.query.order_by(Time.id)
    user_id = StringField('Username', validators=[DataRequired()])
    admin_id = RadioField('Admin', choices=[('1','Anwar Ali'), ('2', 'Bikas Shrestha')] , validators=[DataRequired()], coerce=int)
    date = DateField('Date', validators=[DataRequired()])
    timeslot_id = SelectField('Select Time Period', choices=[(alltimeslot.id, alltimeslot.slot) for alltimeslot in alltimeslots], validators=[DataRequired()], coerce=int)
    appointment_purpose = TextAreaField('Purpose of Appointment', validators=[DataRequired()])
    duration = StringField('Duration')
    submit = SubmitField('Book Now')
