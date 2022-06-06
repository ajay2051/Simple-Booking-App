from backends import  db
from backends.auth.models import User
# from backends.admin.models import Status


days_slot = db.Table(
    'days_slot', 
    db.Column('id', db.Integer, primary_key=True),
    db.Column('days_id', db.Integer, db.ForeignKey('days.id')),
    db.Column('time_id', db.Integer, db.ForeignKey('time.id'))
)




class Days(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.String, nullable=False)
    day_slot = db.relationship('Time', secondary=days_slot, backref=db.backref('day_slot', lazy=True))

    def __repr__(self):
        return f'{self.name}'






class Time(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slot = db.Column('slot', db.String, nullable=False)
    # day = db.relationship('Days', secondary=days_slot, backref=db.backref('time_day', lazy=True))
    
    def __repr__(self):
        return f'{self.slot}'






class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('Admin', db.String, nullable=False)

    def __repr__(self):
        return f'{self.id}'
        


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False)
    admin_id = db.Column('admin_id', db.Integer, db.ForeignKey('admin.id'), nullable=False)
    date = db.Column('date', db.DateTime, nullable=False) 
    timeslot_id = db.Column('timeslot_id', db.Integer, db.ForeignKey('time.id'), nullable=False)
    appointment_purpose = db.Column('purpose', db.String, nullable=False)
    duration = db.Column('duration', db.String, nullable=False)

    # booking_status = db.relationship('Status', back_populates='booking', cascade='all, delete, delete-orphan')


    def __repr__(self):
        return f'{self.admin_id}'



