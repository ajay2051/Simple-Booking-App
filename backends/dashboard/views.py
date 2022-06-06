from flask import Flask, request, render_template
from flask_login import  login_required


@login_required
def dashboard():
    return render_template('dashboard/dashboard.html', title='Dashboard')