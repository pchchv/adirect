from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    context = {
        'title': 'Interior'
    }
    return render_template('index.html', context=context)

@app.route('/generator')
def generator():
    context = {
        'title': 'Interior'
    }
    return render_template('generator.html', context=context)

@app.route('/crossminus')
def crossminus():
    return render_template('crossminus.html')

@app.route('/inclinator')
def inclinator():
    return render_template('inclinator.html')

@app.route('/lemmatizer')
def lemmatizer():
    return render_template('lemmatizer.html')

@app.route('/synonymizer')
def synonymizer():
    return render_template('synonymizer.html')

@app.route('/wordcount')
def wordcount():
    return render_template('wordcount.html')