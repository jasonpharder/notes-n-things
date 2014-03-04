from flask import Flask
from notesNThings.application.models import courses_model
import json

class CoursesController:
	
	@staticmethod
	def getAll():
		return json.dumps(stubCourses)

	@staticmethod
	def getByName(name):
		return json.dumps(stubCourse)
