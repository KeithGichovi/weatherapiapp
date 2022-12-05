from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
import requests
import json
import os
from form import Form
import math

key = 'f2956c73dc3189c78c159f01aa7d5ad1'

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = os.urandom(32)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()
    city = 'washington'
    weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=' + key)
    contents = json.loads(weather.content)
    weather_display = {
        'city': city.capitalize(),
        'country': contents['sys']['country'],
        'temperature': math.ceil(contents['main']['temp']),
        'description': contents['weather'][0]['description'],
        'icon': contents['weather'][0]['icon'],
        'wind_speed': contents['wind']['speed'],
        'wind_direction': contents['wind']['deg'],
        'min_temp': math.ceil(contents['main']['temp_min']),
        'max_temp': math.ceil(contents['main']['temp_max']),
      #  'temp_difference': math.ceil(contents['main']['temp_max'] - contents['main']['temp_min'])
    }
    return render_template('index.html', weather_display=weather_display, form=form)


if __name__ == '__main__':
    app.run(debug=True)
