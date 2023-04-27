from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from map.map import map

cities = list(map)
class ShippingForm(FlaskForm):
    sender = StringField("Sender", validators=[DataRequired()])
    recipient = StringField("Recipient", validators=[DataRequired()])
    origin = SelectField('Origin', coerce=str, choices=cities)
    destination = SelectField('Origin', coerce=str, choices=cities)
    express = BooleanField("Express Shipping?")
    submit = SubmitField("Submit")
    cancel = SubmitField("Cancel")
    
    