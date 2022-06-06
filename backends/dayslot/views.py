from backends import db
from flask_login import login_required, current_user
from .models import Days, Time, Admin, Booking, days_slot
from .forms import DayForm, AdminForm, AdminUpdateForm, BookAppointment
from flask import Flask, request, render_template, url_for, flash, redirect, jsonify, session


@login_required
def day():
    form = DayForm()
    alltimeslots = Time.query.order_by(Time.id)
    if request.method == 'POST':
        days = Days.query.filter_by(name=form.add_day.data).first()
        if days:
            flash('Day already exists')
        if days is None:
            name=form.add_day.data
            timeslots=request.form.getlist('timeslot_id')
            days = Days(name=name)
            for timeslot in timeslots:
                time = Time(slot=timeslot)
                print(timeslots)
                days.day_slot.append(time)
            db.session.add(days)
            db.session.commit()
        alldays = Days.query.order_by(Days.id)
        return redirect(url_for('alldays'))
        return render_template('dayslot/days.html', days=days, alldays=alldays, form=form)
    return render_template('dayslot/days.html', form=form, alltimeslots=alltimeslots )
            



@login_required
def alldays():
     alldays = Days.query.order_by(Days.id)
     return render_template('dayslot/alldays.html', alldays=alldays)



@login_required
def deleteday(id):
    day = Days.query.get_or_404(id)
    db.session.delete(day)
    db.session.commit()
    return redirect(url_for('alldays'))



@login_required
def timeslot():
    form = TimeSlot()
    if form.validate_on_submit():
        time = Time.query.filter_by(slot = form.time_slot.data).first()
        if time:
            flash('Time Slot already exists')
        if time is None:
            time = Time(slot=form.time_slot.data)
            db.session.add(time)
            db.session.commit()
        alltimes = Time.query.order_by(Time.id)
        return redirect(url_for('allslots'))
        return render_template('dayslot/time.html', time=time, alltimes=alltimes, form=form)
    return render_template('dayslot/time.html', form=form)
            


@login_required
def allslots():
    alltimeslots = Time.query.order_by(Time.id)
    return render_template('dayslot/allslots.html', alltimeslots=alltimeslots)


@login_required
def deleteslots(id):
    timeslot = Time.query.get_or_404(id)
    db.session.delete(timeslot)
    db.session.commit()
    return redirect(url_for('allslots'))



@login_required
def admin():
    form = AdminForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(name=form.admin.data).first()
        if admin:
            flash('Admin Already Exists')
        if admin is None:
            admin = Admin(name=form.admin.data)
            db.session.add(admin)
            db.session.commit()
        alladmins = Admin.query.order_by(Admin.id)
        return redirect(url_for('alladmins'))
        return render_template('dayslot/admin.html', admin=admin,form=form, alladmins=alladmins)
    return render_template('dayslot/admin.html', form=form )
        


@login_required
def alladmins():
    alladmins = Admin.query.order_by(Admin.id)
    return render_template('dayslot/alladmins.html', alladmins=alladmins)



@login_required
def updateadmin(id):
    form=AdminUpdateForm()
    admin = Admin.query.get_or_404(id)
    if form.validate_on_submit():
        admin.name = form.admin.data
        db.session.commit()
        return redirect(url_for('alladmins'))
    elif request.method == 'GET':
        form.admin.data = admin.name
    return render_template('dayslot/updateadmin.html', form=form)




@login_required
def deleteadmin(id):
    admin = Admin.query.get_or_404(id)
    db.session.delete(admin)
    db.session.commit()
    return redirect(url_for('alladmins'))



@login_required
def bookappointment():
    form = BookAppointment()
    alladmins = Admin.query.order_by(Admin.id)
    alldays = Days.query.order_by(Days.id)
    alltimeslots = Time.query.order_by(Time.id)
    if request.method == 'POST':
        user_id= int(request.form.get('user_id'))
        print(type(user_id))
        admin_id = int(request.form.get('admin_id'))
        print(type(admin_id))
        date=request.form.get('date')
        timeslot_id = int(request.form.get('timeslot_id'))
        appointment_purpose = request.form.get('appointment_purpose')
        duration = request.form.get('duration') 

        time_slot = Booking.query.filter_by(timeslot_id=timeslot_id).all()
        print(time_slot)

        ts=[]
        for t in time_slot:
            a = t.timeslot_id
            ts.append(a)
        
    
        

        add_id = Booking.query.filter(Booking.admin_id==admin_id).all()
        print(add_id)
        adid = []
        for a in add_id:
            s = a.admin_id
            adid.append(s)
        print(adid)

        u_id = current_user.get_id()

        



            
        
        if  (((u_id) and (timeslot_id in ts)) or (admin_id in adid)):
        
            flash('Booking in this date and this timeslot with this admin Has been Done')
        else:
            appointments=Booking(user_id=user_id,
                                admin_id = admin_id,
                                date=date,
                                timeslot_id = timeslot_id,
                                appointment_purpose = appointment_purpose,
                                duration = duration)
            db.session.add(appointments)
            db.session.commit()
            flash('Booking Successfull')
        return redirect(url_for('dashboard'))
    return render_template('dayslot/bookappointment.html', alladmins=alladmins, alldays=alldays, alltimeslots=alltimeslots, form=form)
        
        
            
        


# def datetimeslot():
#     date= request.args.get('date')
#     date_time_slot = request.args.get('timeslot')
#     print((date_time_slot))
#     timeslot = db.session.query(days_slot).filter(days_slot.days_id==date).all()
#     # timeslot = Time.query.all()
#     for t in timeslot:
#         print((t.slot))
#     print((timeslot))
#     return render_template('dayslot/ajax.html', timeslot=timeslot)
    # return f' {date} has only this time slot {date_time_slot}'
    
        



    




    
        

    
