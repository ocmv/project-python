from wtforms import Form,  HiddenField
from wtforms import validators
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.fields.html5 import EmailField
from .models import User
#validacion nombre usuario no permitido
def admin_validator(form, field):
	if field.data == 'admin' or field.data == 'admin':
		raise validators.ValidationError('El username admin no es permitido')

#validacion honeypot
def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('Solo los humanos pueden completar el registro!')
class LoginForm(Form):
	username = StringField('Username', [
		validators.length(min=4, max=50, message='El username se encuantra fuera de rango'),
	])

	password = PasswordField('Password', [
		validators.Required(message='El password es requerido'),
	])

class RegisterForm(Form):
	username = StringField('Username', [
		validators.length(min=4, max=50),
		admin_validator
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

	accept = BooleanField('', [
		validators.DataRequired()
	])

	honeypot = HiddenField("", [ length_honeypot] )

	#validacion de campos: validate_campoavalidar
	def validate_username(self, username):
		if User.get_by_username(username.data):
			raise validators.ValidationError('El username ya se encuentra en uso')
	
	def validate_email(self, email):
		if User.get_by_email(email.data):
			raise validators.ValidationError('El email ya se encuentra en uso')

	#para sobreescribir metodo validate
	def validate(self):
		if not Form.validate(self):
			return False

		if len(self.password.data) < 6:
			self.password.errors.append('El password es demasiado corto')
			return False
		return True

class TaskForm(Form):
	title = StringField('Titulo',[
		validators.length(min=6, max=50),
		validators.DataRequired(message='El titulo es requerido'),
	])

	description = TextAreaField('Descripcion',[
		validators.DataRequired(message='La descripcion es requerida'),
	], render_kw={'rows': 5})