from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, IntegerField, SubmitField, EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    password_again = PasswordField(validators=[DataRequired()])
    surname = StringField(validators=[DataRequired()])
    name = StringField(validators=[DataRequired()])
    age = IntegerField(validators=[DataRequired()])
    position = StringField(validators=[DataRequired()])
    speciality = StringField(validators=[DataRequired()])
    address = StringField(validators=[DataRequired()])
    submit = SubmitField()