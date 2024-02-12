# app.py (Flask приложение)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Добро пожаловать на страницу миссии на Марс!"

@app.route('/training/<prof>')
def training(prof):
    return render_template('base.html', prof=prof)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
