from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length

class ContactForm(FlaskForm):
    """Contact form."""
    user_name = StringField('Name', [DataRequired(),Length(min=4, message=('Your message is too short.'))])
    user_email = StringField('Email', [DataRequired(),Length(min=4, message=('Your message is too short.'))])
    body = StringField('Message', [DataRequired(),Length(min=4, message=('Your message is too short.'))])
    submit = SubmitField('Submit')