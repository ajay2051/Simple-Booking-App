from backends import db
from flask import Flask, request, render_template, url_for, flash, redirect
from flask_login import current_user, login_required
from backends.dayslot.models import Booking
from .forms import ApprovalForm
from .models import Status
from flask import session



@login_required
def adminpage():
    bookings = Booking.query.all()
    id = current_user.id
    if id == 2 or id ==3 :
        return render_template('admin/admin.html', bookings=bookings)
    else:
        flash('You Are Not Authorized To Access This Page. Only Admins Can Have Access This Page')
        return redirect(url_for('dashboard'))


@login_required
def status():
    form = ApprovalForm()
    bookings = Booking.query.all()
    if request.method == 'POST':
        booking_id = int(request.form.get('booking_id'))
        status = int(request.form.get('status'))
        approve = Status(booking_id =booking_id,
                status = status)
        book_ids = Booking.query.filter_by(id=booking_id).all()
        db.session.add(approve)
        db.session.commit()
        for i in book_ids:
            if approve.status == 0:
                db.session.delete(i)
                db.session.commit()
                flash('Booking Has been rejected successfully')
            else:
                flash('Booking Approved')
        return redirect(url_for('dashboard'))
        return render_template('admin/status.html', booking_id=booking_id)
    return render_template('admin/status.html', title='Status', form=form, bookings=bookings)
        
        
        
        
    
