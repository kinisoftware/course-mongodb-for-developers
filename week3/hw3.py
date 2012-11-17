import pymongo

connection = pymongo.Connection()
school = connection.school

students = school.students

query = {'scores.type':'homework'}
docs = students.find(query)

for doc in docs:
	lowest_score = 100.0
	score_with_lowest_score = {}
	scores = doc['scores']
	for score in scores:
		if score['type'] == 'homework' :
			if score['score'] < lowest_score :
				lowest_score = score['score']
				score_with_lowest_score = score
	scores.remove(score_with_lowest_score)
	doc['scores'] = scores
	students.update({'_id' : doc['_id']}, doc, upsert=False)