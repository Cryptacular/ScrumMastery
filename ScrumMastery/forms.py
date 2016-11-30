from flask_wtf import Form
from wtforms.fields import StringField, PasswordField
from wtforms.validators import DataRequired, email


class CreateAccountForm(Form):
    email = StringField('email', validators=[DataRequired(), email()])
    password = PasswordField('password', validators=[DataRequired()])