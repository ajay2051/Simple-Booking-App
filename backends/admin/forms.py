from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.validators import DataRequired
from wtforms import IntegerField, RadioField, SubmitField, StringField

class ApprovalForm(FlaskForm):
    id = IntegerField('id')
    booking_id = StringField('Booking_id')
    status = RadioField(choices=[('1','Approved'), ('0', 'Rejected')], validators=[DataRequired()], default=0)
    submit = SubmitField('Submit')