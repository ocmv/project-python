from wtforms import Form
from wtforms import validators
from wtforms import StringField, PasswordField, BooleanField
from wtforms.fields.html5 import EmailField
class LoginForm(Form):
	username = StringField('Username', [
		validators.length(min=4, max=50, message='El username se encuantra fuera de rango')
	])

	password = PasswordField('Password', [
		validators.Required(message='El password es requerido'),
	])

class RegisterForm(Form):
	username = StringField('Username', [
		validators.length(min=4, max=50)
	])

	email = EmailField('Correo electronico', [
		validators.length(min=6, max=100),
		validators.Required(message='El email es requerido'),
		validators.Email(message='Ingrese un email valido'),
	])

	password = PasswordField('Password', [
		validators.Required(message='El password es requerido'),
		validators.EqualTo('confirm_password', message='La contraseña no coincide')
	])

	confirm_password = PasswordField('Confirme contraseña')

	accept = BooleanField('Acepto terminosy condiciones', [
		validators.DataRequired()
	])