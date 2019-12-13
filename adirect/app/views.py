from flask import Flask, request, render_template
from .processors import modifier, counter, generator, lemma, cityremover, trim_utm, synonym, crossminus, declension


application = Flask(__name__)


@application.route('/')
def index():
    return render_template('index.html', title='Home', ServiceName='Сделаем это!')


@application.route('/team')
def team():
    return render_template('team.html', title='Считалка слов', ServiceName='Считалка слов')


@application.route('/keyword/generator')
def Generator():
    return render_template('/keyword/generator.html', title='Генератор фраз', ServiceName='Генератор фраз')


@application.route('/keyword/generator/submit', methods=['GET', 'POST'])  # принимает текст
def ServiceGenerator():
    colamn = []
    colamn.append(modifier(request.form["colamn0"], 'all'))
    colamn.append(modifier(request.form["colamn1"], 'all'))
    colamn.append(modifier(request.form["colamn2"], 'all'))
    colamn.append(modifier(request.form["colamn3"], 'all'))
    colamn.append(modifier(request.form["colamn4"], 'all'))
    colamn.append(modifier(request.form["colamn5"], 'all'))
    colamn.append(modifier(request.form["colamn6"], 'all'))

    words = generator(colamn)

    return render_template('/keyword/generator.html', title='Генератор фраз', ServiceName='Генератор фраз',
                           result=words)


@application.route('/keyword/crossminus', methods=['GET', 'POST'])
def CrossMinus():
    return render_template('/keyword/crossminus.html', title='Кросс-минусовка фраз', ServiceName='Кросс-минусовка фраз')


@application.route('/keyword/crossminus/submit', methods=['GET', 'POST'])  # принимает текст
def ServiceCrossminus():
    words = crossminus(modifier(request.form["words"], 'all'))

    return render_template('/keyword/crossminus.html', title='Кросс-минусовка фраз', ServiceName='Кросс-минусовка фраз',
                           result=words)


@application.route('/keyword/inclinator')
def inclinator():
    return render_template('/keyword/inclinator.html', title='Склонятор', ServiceName='Склонение ключевых слов')


@application.route('/keyword/inclinator/submit', methods=['GET', 'POST'])  # принимает текст
def ServiceInclinator():
    words = declension(modifier(request.form["words"], 'all'))

    return render_template('/keyword/inclinator.html', title='Склонятор', ServiceName='Склонение ключевых слов',
                           result='\n'.join(words))

@application.route('/keyword/lemmatizer')
def lemmatizer():

    return render_template('/keyword/lemmatizer.html', title='Лемматизатор', ServiceName='Лемматизатор')


@application.route('/keyword/lemmatizer/submit', methods=['GET', 'POST'])  # принимает текст
def inclinatorLemmatizer():
    words = lemma(modifier(request.form["words"], 'all'))

    return render_template('/keyword/lemmatizer.html', title='Лемматизатор', ServiceName='Лемматизатор', result=words)


@application.route('/keyword/synonymizer')
def synonymizer():
    return render_template('/keyword/synonymizer.html', title='Синонимайзер', ServiceName='Синонимайзер')


@application.route('/keyword/synonymizer/submit', methods=['GET', 'POST'])  # принимает текст
def ServiceSynonymizer():
    words = synonym(request.form["words"])

    return render_template('/keyword/synonymizer.html', title='Синонимайзер', ServiceName='Синонимайзер', result=words)


@application.route('/keyword/wordcount')
def wordcount():
    return render_template('/keyword/wordcount.html', title='Считалка слов', ServiceName='Считалка слов')


@application.route('/keyword/wordcount/submit', methods=['GET', 'POST'])  # принимает текст
def ServiceWordcount():
    words = counter(modifier(request.form["words"], 'allpasswrap'))

    return render_template('/keyword/wordcount.html', title='Считалка слов', ServiceName='Считалка слов', result=words)


@application.route('/keyword/trimutm')
def TrimUtm():
    return render_template('/keyword/trimutm.html', title='Удаление UTM меток', ServiceName='Удаление UTM меток')


@application.route('/keyword/trimutm/submit', methods=['GET', 'POST'])  # принимает текст
def ServiceTrimUtm():
    words = trim_utm(request.form["words"])

    return render_template('/keyword/trimutm.html', title='Удаление UTM меток', ServiceName='Удаление UTM меток',
                           result=words)


@application.route('/keyword/cityremover')
def CityRemover():
    return render_template('/keyword/cityremover.html', title='Удаление городов', ServiceName='Удаление городов')


@application.route('/keyword/cityremover/submit', methods=['GET', 'POST'])  # принимает текст
def ServiceCityRemover():
    words = cityremover(modifier(request.form["words"], 'all'))

    return render_template('/keyword/cityremover.html', title='Удаление городов', ServiceName='Удаление городов',
                           result=words)
