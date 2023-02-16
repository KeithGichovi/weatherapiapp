from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import requests
import json
import os
from form import checkWeather
import math
from datetime import date
key = 'd3a3a75852a441e51b6310f03db07a03'

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = os.urandom(32)


@app.route('/', methods=['GET', 'POST'])
def index():
    today = date.today()
    d1 = today.strftime("%d-%m-%Y")
    form = checkWeather()
    city = None
    if form.validate_on_submit():
        city = form.location.data

    weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=' + key)
    contents = json.loads(weather.content)
    weather_display = {
            'city': city,
            'country': contents['sys']['country'],
            'temperature': math.ceil(contents['main']['temp']),
            'description': contents['weather'][0]['description'],
            'icon': contents['weather'][0]['icon'],
            'wind_speed': contents['wind']['speed'],
            'wind_direction': contents['wind']['deg'],
            'min_temp': math.ceil(contents['main']['temp_min']),
            'max_temp': math.ceil(contents['main']['temp_max']),
    }
    return render_template('index.html', weather_display=weather_display, form=form, d1=d1)


if __name__ == '__main__':
    app.run(debug=True)
