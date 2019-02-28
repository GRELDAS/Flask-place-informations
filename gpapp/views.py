""" Views """

from flask import Flask, render_template, session, request, json, jsonify
from gpapp.scripts.geocoder import Geocoder
from gpapp.scripts.parser import Parser
from gpapp.scripts.searcher import Searcher

import time

# App config
DEBUG = True
app = Flask(__name__)
app.config.from_object('config')
app.config['SECRET_KEY'] = '7d441f27d442147867d44ju1f2b6176a'

@app.route('/', methods=['GET', 'POST'])
@app.route('/index/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/_query', methods=['GET', 'POST'])
def query():

        if request.method == 'POST':

                user_request = request.form['user_request']

                parser = Parser(sentence=user_request)
                parser.sentence_parsing()

                geocoder = Geocoder(request=parser.request_keywords)
                geocoder.get_coordinates()

                searcher = Searcher(request=parser.request_keywords)
                searcher.get_data()

                time.sleep(5)

                return jsonify(
                        long=geocoder.coordinates[0],
                        lat=geocoder.coordinates[1],
                        address=geocoder.address,
                        response=searcher.data)
