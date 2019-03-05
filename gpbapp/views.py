""" Views """

from flask import Flask, render_template, session, request, json, jsonify
from gpbapp.scripts.grandpy import GrandPy

import time

# App config
app = Flask(__name__)
app.config['SECRET_KEY'] = '7d441f27d442147867d44ju1f2b6176a'

@app.route('/', methods=['GET', 'POST'])
@app.route('/index/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/_query', methods=['GET', 'POST'])
def query():

        if request.method == 'POST':

                user_request = request.form['user_request']

                grandpy = GrandPy()
                grandpy.get_response(sentence=user_request)

                time.sleep(2)

        return jsonify(address=grandpy.address, address_story=grandpy.address_story)
