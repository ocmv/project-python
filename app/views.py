from flask import Blueprint
from flask import render_template, request, flash, redirect, url_for

from flask_login import login_user, logout_user
from .forms import LoginForm, RegisterForm
from .models import User
from . import login_manager
page = Blueprint('page', __name__)

@login_manager.user_loader
def load_user(id):
	return User.get_by_id(id)
	
@page.app_errorhandler(404)
def page_not_found(error):
	return render_template('errors/404.html'), 404

@page.route('/')
def index():
	return render_template('index.html', title='index')

@page.route('/logout')
def logout():
	logout_user()
	flash('Cerraste sesion exitosamente')
	return redirect(url_for('.login'))

@page.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm(request.form)

	if request.method == 'POST' and form.validate():
		user = User.get_by_username(form.username.data)
		if user and user.verify_password(form.password.data):
			login_user(user)
			flash('Usuario autenticado exitosamente')
		else:
			flash('Usuario o password incorrectos','error')
	return render_template('auth/login.html', title='login', form=form)

@page.route('/register', methods=['GET','POST'])
def register():
	form = RegisterForm(request.form)
	if request.method == 'POST':
		if form.validate():
			user = User.create_element(form.username.data, form.password.data, form.email.data)
			flash('Usuario registrado exitosamente')
	return render_template('auth/register.html', title='Registro', form=form)

@page.route('/tasks')
def tasks():
	return render_template('task/list.html', title='Tareas')