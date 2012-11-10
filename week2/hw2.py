import pymongo

connection = pymongo.Connection()
students = connection.students

grades = students.grades

query = {'type':'homework'}
sort_clauses = [('student_id', pymongo.ASCENDING),('score', pymongo.ASCENDING)]
docs = grades.find(query).sort(sort_clauses)

student_id = -1
for doc in docs:
	if student_id is -1 :
		grades.remove(doc)
	elif student_id is not doc['student_id'] :
		grades.remove(doc)
	student_id = doc['student_id']