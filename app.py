from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from form import checkWeather
import meteomatics
import datetime
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'encryptedkey'





@app.route('/', methods=['GET', 'POST'])
def index():
    form = checkWeather()
    form.location = None
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
