from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, AddForm
from app.models import User


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations,User Registered!')
        return redirect(url_for('add'))   
    return render_template('login.html', title='user', form=form)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        user1 = User(username=form.username1.data)
        user1.set_password(form.password1.data)
        db.session.add(user1)
        user2 = User(username=form.username2.data)
        user2.set_password(form.password2.data)
        db.session.add(user2)
        db.session.commit()
        flash('Congratulations,Users Registered!')   
    return render_template('add.html', title='add', form=form)
