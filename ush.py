# app.py (Flask приложение)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Добро пожаловать на страницу миссии на Марс!"

@app.route('/<list_prof>/<list2>')
def training(list_prof, list2):
    print(list2, list_prof)
    return render_template('base.html', list_prof=list_prof, list2=list2)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
