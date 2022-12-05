from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class Form(FlaskForm):
    city = StringField(label="Enter the name of the city:", validators=[DataRequired()])
    submit = SubmitField(label="Search weather")
