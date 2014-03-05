from flask import Flask
from notesNThings.application.models import courses_model
import json

class CoursesController:
	
	@staticmethod
	def getAll():
		return courses_model.getAllCourses()

	@staticmethod
	def getByName(name):
		return courses_model.getAllCourses()
