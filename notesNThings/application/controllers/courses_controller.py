from flask import Flask
from notesNThings.application.models import courses_model
import json

class CoursesController:
	
	@staticmethod
	def getAll():
		stubCourses = {'courses': [ 
			{'id': 0, 'courseID': '0', 'term': None, 'name': 'COMP 1010', 'alt_name': "Always be brogramming all the time", 'professor': None}, 
			{'id': 1, 'courseID': '1', 'term': None, 'name': 'COMP 1020', 'alt_name': "Brogramming 2.0", 'professor': None} ]
		}
		return json.dumps(stubCourses)

	@staticmethod
	def getByName(name):
		stubCourse = {'courseID': 0, 'term': None, 'name': 'COMP 1010', 'alt_name': "Always be brogramming all the time", 'professor': None}
		return json.dumps(stubCourse)
