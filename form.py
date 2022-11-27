from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, InputRequired


class checkWeather(FlaskForm):
    location = StringField("Enter location to check weather", validators=[DataRequired(), InputRequired()])
    submit = SubmitField("Check weather.")
