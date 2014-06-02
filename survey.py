import os
import csv
import random
import datetime

def _match_score(my_answer, mentor_answer):
	matches = 0
	for (a,b) in zip(my_answer, mentor_answer):
	    if a==b:
	        matches +=1
	return matches

def dummy_match(my_answer):
    return 1


def get_mentor_match(my_answer, mentors):
    best_score = 0
    best_mentor = random.choice(mentors.keys()) #if no match to any mentors, randomly select one
    for k in mentors.keys():
        #for each mentor, find score
        score = _match_score(my_answer,mentors[k])
        if score > best_score:
            best_score = score
            best_mentor = k
    return best_mentor

def load_mentor_answers(filename):
    mentors = {}
    f = open("static/"+filename)
    lines = f.read().split("\r")
    for line in lines[1:]:
        row = line.split(',')
        mentors[row[0]] = row[1:]
    return mentors

def load_mentor_profiles(filename, backupfile, csv_file=True):

    mentors = {}
    if csv_file:
        f = open("static/" + filename, 'rU')
        fc = csv.reader(f)
        count = 0
        header = []
        for row in fc:
            if len(row)==0:
                continue
            row_stripped = [c.strip() for c in row]
            if count==0:
                header = row_stripped                
            else:
                try:
                    row_stripped = [c.decode('utf-8') for c in row_stripped]
                    name = row_stripped[0]
                    answers = []
                    for e in range(1,len(header)):
                        if row_stripped[e] != 'pass' and row_stripped[e] != 'PASS' and row_stripped[e]!='':
                            answers.append([header[e],row_stripped[e]])
                    mentors[name] = answers
                except:
                    print row_stripped
            count+=1
        f = open("static/" + filename, 'rU')
        fc = csv.reader(f)
        count = 0
        header = []
        for row in fc:
            if len(row)==0:
                continue
            row_stripped = [c.strip() for c in row]
            if count==0:
                header = row_stripped                
            else:
                try:
                    row_stripped = [c.decode('utf-8') for c in row_stripped]
                    name = row_stripped[0]
                    answers = []
                    for e in range(1,len(header)):
                        if row_stripped[e] != 'pass' and row_stripped[e] != 'PASS' and row_stripped[e]!='':
                            answers.append([header[e],row_stripped[e]])
                    if name not in mentors.keys():
                        mentors[name] = answers
                except:
                    print row_stripped
            count+=1
        return mentors
    else:
        f = open("static/"+filename)
        lines = f.read().split("\r")
        header = lines[0].split('\t')
        for line in lines[1:]:
            row = line.split('\t')
            name = row[0]
            answers = []
            for e in range(1,len(header)):
                if row[e] != 'pass' and row[e] != 'PASS' and row[e]!='':
                    answers.append([header[e],row[e]])
            mentors[name] = answers
        return mentors

def _load_questions(filename):
    questions = {}
    f = open("static/"+filename)
    lines = f.read().split("\r")
    for line in lines[1:]:
        row = line.split(',')
        questions[row[0]] = row[1:]
    return questions

def load_questions(filename):
    questions = []
    f = open("static/"+filename)
    lines = f.read().split("\r")
    for line in lines[1:]:
        row = line.split(',')
        row = [r for r in row if r!='']
        questions.append(row)
    return questions

def load_mentor_names(filename):
    links = {}
    links_rev = {}
    f = open("static/"+filename)
    lines = f.read().split("\r")
    for line in lines[1:]:
        row = line.split(',')
        links[row[0]] = row[1]
        links_rev[row[1]] = row[0]
    return links, links_rev

def write_log_file(file, line):
	if not os.path.exists(file): 
		open(file, 'w').close() 

	with open(file, "a") as myfile:
		myfile.write(str(datetime.datetime.today()) + "\t" + line + "\n")

def add_answer_to_db(answer, db = 'file'):
    TBL_NAME = 'responses'
    timestamp = datetime.today()
    sql_cmd = "INSERT " + ','.join(answer) + " INTO " + responses + ";"
    sql_cmd += "COMMIT;"    
    #create new cursor
    if db=='file':
        print answer
    elif db=='mysql':
    #execute ecommand
        msg = cur.execute(sql_cmd)
        return msg

def main(answers, logfile = "database.log", mentor_files = "mentor_profiles.csv"):
	#given answers, return page to go to and 
	#also store answer

	#
	msg = add_answer_to_db(answers)
	mentors = load_mentor_answers(mentor_files)
	match = get_mentor_match(answers, mentors)
	return match



