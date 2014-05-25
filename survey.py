import csv
import random
import datetime

answer = [] #array of answers
mentors = {} #dictionary of mentor answers



def _match_score(my_answer, mentor_answer):
	matches = 0
	for (a,b) in zip(my_answer, mentor_answer):
		if a==b:
			matches +=1
	return matches

def get_mentor_match(my_answer, mentors):
	best_score = 0
	best_mentor = random.choice(mentors.keys()) #if no match to any mentors, randomly select one
	for k in mentors.keys():
		#for each mentor, find score
		score = _match_score(my_answer,mentors[k])
		if score > best_score:
			best_score = score
			best_mentor = k
	return k

def load_mentor_profiles(filename):
	mentors = {}
	f =csv.reader(filename, dialect='excel')
	for row in f:
		mentors[row[0]] = row[1:]
	return mentors

def add_answer_to_db(answer):
	TBL_NAME = 'responses'
	timestamp = datetime.now()
	sql_cmd = "INSERT " + ','.join(answer) + " INTO " + responses + ";"
	sql_cmd += "COMMIT;"	
	#create new cursor

	#execute ecommand
	msg = cur.execute(sql_cmd)
	return msg

def main(answers, logfile = "database.log", mentor_files = "mentor_profiles.csv"):
	#given answers, return page to go to and 
	#also store answer

	#
	msg = add_answer_to_db(answers)
	mentors = load_mentor_profiles(mentor_files)
	match = get_mentor_match(answers, mentors)
	return match



