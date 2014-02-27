from flask import Flask
import json

class CoursesController:
	
	@staticmethod
	def getAll():
		stubCourses = [ {'courseID': 0, 'term': None, 'name': 'COMP 1010', 'alt_name': "Always be brogramming all the time", 'professor': None}, {'courseID': 1, 'term': None, 'name': 'COMP 1020', 'alt_name': "Brogramming 2.0", 'professor': None} ]
		return json.dumps(stubCourses)

	@staticmethod
	def getByName(name):
		stubCourse = {'courseID': 0, 'term': None, 'name': 'COMP 1010', 'alt_name': "Always be brogramming all the time", 'professor': None}
		return json.dumps(stubCourse)
