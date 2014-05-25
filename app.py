#!/usr/bin/env python

import os

from flask import Flask
from flask import url_for
from flask import render_template
from flask import jsonify
from flask import url_for
from flask import request


app = Flask(__name__)

#f = open("static/data.tsv", 'r')



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/survey', methods=['POST'])
def result():
    search = request.args.getlist('search')[0].decode('utf-8')

    return render_template('finitescroll.html', query=search, totalresults = total, searchJSON=idGroups, searchJSON2=[idGroupsHash])

@app.route('/result2', methods=['GET', 'POST'])
def result2():
    recipeids = request.form.getlist('links[]')

    return render_template('variations.html', query=search, totalresults = total, searchJSON=searchjsonObject, searchJSON2=searchjsonObject2)

@app.route('/recipes', methods=['GET', 'POST'])
def recipes():
    links = request.form.getlist('links[]')

    return render_template('test.html', links = links)

@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/howitworks')
def howitworks():
    return render_template('howitworks.html')

@app.route('/data')
def data():
    return render_template('analysis.html')

@app.route('/contact')
def contact():
    return render_template('about.html')
    
@app.route('/api')
def api():
    recommendation = {'band':'radiohead', 'album':'Ok Computer'}
    return jsonify(recommendation)


@app.route('/broken')
def broken():
    var = does_not_exist
    return jsonify(recommendation)


@app.route('/bootstrap')
def bootstrap():
    return render_template('bootstrap.html')


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0',port=8080)
#      app.run(host='192.168.1.28', port=8000)

    
