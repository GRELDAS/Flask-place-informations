from flask import Flask, render_template, session, request, json
from gpapp.parser import Parser

# App config
DEBUG = True
app = Flask(__name__)
app.config.from_object('config')
app.config['SECRET_KEY'] = '7d441f27d442147867d44ju1f2b6176a'
new_parser = Parser()

@app.route('/', methods=['GET', 'POST'])
@app.route('/index/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_parser.split(text=request.form["research"])
    return render_template('index.html')