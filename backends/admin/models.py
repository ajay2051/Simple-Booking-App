from backends import db
from backends.dayslot.models import Booking


class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column('booking_id', db.Integer, db.ForeignKey('booking.id', ondelete="CASCADE"))
    status = db.Column('status', db.Integer, nullable=False)
    # booking = db.relationship('Booking', back_populates='booking_status')
