from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo

class RegistroForm(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired()])
    contraseña = PasswordField('Contraseña', validators=[DataRequired(), EqualTo('confirmar_contraseña', message='Las contraseñas deben coincidir')])
    confirmar_contraseña = PasswordField('Confirmar Contraseña', validators=[DataRequired()])
    nombre_completo = StringField('Nombre Completo', validators=[DataRequired()])
    puesto = StringField('Puesto', validators=[DataRequired()])
    recaptcha = RecaptchaField()
    enviar = SubmitField('Registrarse')

class LoginForm(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired()])
    contraseña = PasswordField('Contraseña', validators=[DataRequired()])
    recordarme = BooleanField('Recordarme')
    recaptcha = RecaptchaField()
    enviar = SubmitField('Iniciar Sesión')
