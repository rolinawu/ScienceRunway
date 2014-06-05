#!/usr/bin/env python

import os
import json

from flask import Flask
from flask import url_for
from flask import render_template
from flask import jsonify
from flask import url_for
from flask import request
from survey import * 

#host_set = '54.200.171.124'
host_set = '0.0.0.0'
port_set = 8080

app = Flask(__name__)
MAILING_LIST = "mailing_list.txt"
SURVEY_RESULTS = "survey_results.txt"
#f = open("static/data.tsv", 'r')

#links, links_rev = load_mentor_names("mentors_links.csv")
links, links_rev = load_mentor_names("mentor_links_final.csv")
#mentors = load_mentor_answers("mentors_quiz.csv")
mentors = load_mentor_answers("mentor_answers.csv")
#questions = load_questions("questions.csv")
questions = load_questions("questions_final.csv")
#profiles = load_mentor_profiles("mentor_profiles.txt")
profiles = load_mentor_profiles("mentor_profilesfinalv2.csv", "mentor_profilesfinalv3.csv", csv_file = True)
#print mentors


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/mailing', methods=['GET','POST'])
def mailing():
    q1 = request.args
    email = q1['comments']
    if email!='':
        write_log_file(MAILING_LIST, email)
    return render_template('thanks.html')

@app.route('/gallery')
def gallery():
    mk = links.keys()
    random.shuffle(mk)
    return render_template('gallery.html', images = mk[:16], profiles = profiles)

@app.route('/quiz', methods=['GET','POST'])
def survey():
    return render_template('survey.html', questions = questions)

@app.route('/result', methods=['GET', 'POST'])
def result():
    q1 = request.args
    name = q1['name']
    if name=='Your name' or name=='':
        name = ''
    else:
        name = " " + name

    answer = []
    #assume that all questions have been answered; in future will have to add check to html to block incomplete answers
    for i in range(len(questions)):
        question_key = "Q" + str(i + 1)
        if question_key in q1.keys():
            answer.append(q1[question_key])
        else:
            answer.append("")
    match = get_mentor_match(answer, mentors)
#    q1 = request.args.getlist('Q1').decode('utf-8')
    write_log_file(SURVEY_RESULTS, json.dumps(q1) + "\tMATCHED TO: %s"% match)
    return render_template("profile.html", message1 = "Congratulations%s!"%name, message2 = "Your mentor is: ", name = links[match], key = match, profile = profiles[match])


@app.route('/profile', methods=['GET'])
def profile():
    q1 = request.args
    key = q1['key']
    print profiles[key]
    return render_template('profile.html', name = links[key], key = key, profile = profiles[key])

    #change

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.                                                               
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host=host_set,port=port_set)
#      app.run(host='192.168.1.28', port=8000)                                                                          

    
