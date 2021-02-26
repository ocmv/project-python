from flask import Blueprint
from flask import render_template, request

from .forms import LoginForm, RegisterForm
from .models import User

page = Blueprint('page', __name__)

@page.app_errorhandler(404)
def page_not_found(error):
	return render_template('errors/404.html'), 404

@page.route('/')
def index():
	return render_template('index.html', title='index')

@page.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm(request.form)

	if request.method == 'POST' and form.validate():
		print("nueva sesion creada")
	return render_template('auth/login.html', title='login', form=form)

@page.route('/register', methods=['GET','POST'])
def register():
	form = RegisterForm(request.form)
	if request.method == 'POST':
		if form.validate():
			user = User.create_element(form.username.data, form.password.data, form.email.data)
			print("usuario creado exitosa")
			print(user.id)
	return render_template('auth/register.html', title='Registro', form=form)