from flask import Flask
from notesNThings.application.models import courses_model
from notesNThings.application.models.courses_model import Course

import json

class CoursesController:
	
	@staticmethod
	def getAll():
		return courses_model.getAllCourses()

	@staticmethod
	def getByName(name):
		return courses_model.getAllCourses()

def api_post_get_many(result=None, **kw):
	print "api_post_get_many"
	print result['objects']
	result['courses'] = result['objects']
	for key in result.keys():
		#DEBUG Print
		print key 
		if key != 'courses': 
			del result[key]
	for test in result['courses']:
		test['id'] = test['courseID']
		#DEBUG Print
		print test

def create_course_api(restless_manager):
	# Create API endpoints, which will be available at /api/<tablename> by
	# default. Allowed HTTP methods can be specified as well.
	restless_manager.create_api(
		Course,  
		methods=['GET', 'POST', 'DELETE'], 
		url_prefix='/api',
		collection_name='courses',
		postprocessors={
	        'GET_MANY': [api_post_get_many],
	        #'POST': [api_post_get_many],
	        #'PUT_SINGLE': [api_post_get_many]
	    },
	    preprocessors={
	        #'POST': [api_post_get_many],
	        #'PUT_SINGLE': [api_post_get_many]
	    }
	)