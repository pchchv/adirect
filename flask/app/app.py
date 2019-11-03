from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html', title='Home', ServiceName='Сделаем это!')

@app.route('/team')
def team():
    return render_template('team.html', title='Считалка слов', ServiceName='Считалка слов')

@app.route('/keyword/generator', methods=['GET', 'POST'])
def generator():
    return render_template('/keyword/generator.html', title='Генератор фраз', ServiceName='Генератор фраз')

@app.route('/keyword/crossminus')
def crossminus():
    return render_template('/keyword/crossminus.html', title='Кросс-минусовка фраз', ServiceName='Кросс-минусовка фраз')

@app.route('/keyword/inclinator')
def inclinator():
    return render_template('/keyword/inclinator.html', title='Склонятор', ServiceName='Склонение ключевых слов')

@app.route('/keyword/lemmatizer')
def lemmatizer():
    return render_template('/keyword/lemmatizer.html', title='Лемматизатор', ServiceName='Лемматизатор')

@app.route('/keyword/synonymizer')
def synonymizer():
    return render_template('/keyword/synonymizer.html', title='Синонимайзер', ServiceName='Синонимайзер')

@app.route('/keyword/wordcount')
def wordcount():
    return render_template('/keyword/wordcount.html', title='Считалка слов', ServiceName='Считалка слов')

