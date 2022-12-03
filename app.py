from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
import requests
import json


app = Flask(__name__)
bootstrap = Bootstrap5(app)


@app.route('/', methods=['GET'])
def index():
    news_api = requests.get('http://api.weatherstack.com/current?access_key=cca13c8cbd5990a6db63a86ee6c5c490&query=Salisbury')
    contents = json.loads(news_api.content)
    return render_template('index.html', contents=contents)


if __name__ == '__main__':
    app.run(debug=True)
