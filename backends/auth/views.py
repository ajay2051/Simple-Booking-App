from flask import Flask, request, redirect, url_for, render_template, flash
from .forms import RegistrationForm, LoginForm
from .models import User
from backends import  db
from backends import login_manager
from backends import bcrypt
from backends.dashboard.views import dashboard
from flask_login import login_user, logout_user, current_user, login_required, LoginManager, UserMixin



def registration():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form=RegistrationForm()
    if form.validate_on_submit():
        encryptedpassword = bcrypt.generate_password_hash(form.password.data).decode('utf-8', 'ignore')
        users = User(firstname=form.firstname.data, 
        lastname=form.lastname.data, 
        username=form.username.data,
        email=form.email.data , 
        password=encryptedpassword
        
        )
        
        # usertypes = UserType(usertypes=form.usertypes.data)
        db.session.add(users)
        # db.session.add(usertypes)
        db.session.commit()
        
        return redirect(url_for('login'))
    else:
        flash(f'Registration Unsuccessfull for{form.username.data}', category='danger')
    print(form.errors)
    return render_template('auth/registration.html', title='Registration', form=form)

# @login_required
# def registrationsuccessfull():
#     return render_template('auth/registrationsuccessfull.html')


def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form=LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            flash('Invalid Username Password', category='danger')
            return redirect(url_for('login'))
        else:
            if not bcrypt.check_password_hash(user.password, form.password.data):
                flash('Invalid Username Password', category='danger')
                return redirect(url_for('login'))
            else:
                login_user(user)
                return redirect(url_for('dashboard'))
    return render_template('auth/login.html', title='Login', form=form)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))




def logout():
    logout_user()
    return redirect(url_for('login'))
    


