from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html', title='Home', ServiceName='Сделаем это!')

@app.route('/generator')
def generator():

    return render_template('generator.html', title='Генератор фраз', ServiceName='Генератор фраз')

@app.route('/crossminus')
def crossminus():
    return render_template('crossminus.html', title='Кросс-минусовка фраз', ServiceName='Кросс-минусовка фраз')

@app.route('/inclinator')
def inclinator():
    return render_template('inclinator.html', title='Склонятор', ServiceName='Склонение ключевых слов')

@app.route('/lemmatizer')
def lemmatizer():
    return render_template('lemmatizer.html', title='Лемматизатор', ServiceName='Лемматизатор')

@app.route('/synonymizer')
def synonymizer():
    return render_template('synonymizer.html', title='Синонимайзер', ServiceName='Синонимайзер')

@app.route('/wordcount')
def wordcount():
    return render_template('wordcount.html', title='Считалка слов', ServiceName='Считалка слов')