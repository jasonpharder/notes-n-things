from flask import Flask
from notesNThings.application.models import courses_model
from notesNThings.application.models.courses_model import Course
from notesNThings.application.models.notes_model import Note
import json

def api_get_many(result=None, **kw):
	print "COURSE: api_get_many"
	print result['objects']
	result['courses'] = result['objects']
	for key in result.keys():
		print key 
		if key != 'courses': 
			del result[key]
	for test in result['courses']:
		test['id'] = test['courseid']
	print test

def patch_single_preprocessor(instance_id=None, data=None, **kw):
	"""Accepts two arguments, `instance_id`, the primary key of the
	instance of the model to patch, and `data`, the dictionary of fields
	to change on the instance.
	"""
	print "COURSE------------------->patch single preprocessor"
	print data
	#data = data['user'].copy()
	data['name'] = data['course']['name']
	data['alt_name'] = data['course']['alt_name']
	data['professor'] = data['course']['professor']
	del data['course']
	print "DATA AFTER PARSING "+instance_id
	print data

def patch_single_postprocessor(result=None, **kw):
	"""Accepts a single argument, `result`, which is the dictionary
	representation of the requested instance of the model.

	"""
	print "COURSE------------------->patch single postprocessor"
	result['course'] = result.copy()
	for key in result.keys():
		if key != 'course': 
			del result[key]
	
	result['course']['id'] = result['course']['courseid']
	print result	
	pass

def post_preprocessor(data=None, **kw):
	"""Accepts a single argument, `data`, which is the dictionary of
	fields to set on the new instance of the model.

	"""
	print "COURSE------------------->POST  preprocessor"
	print data
	#data = data['user'].copy()
	data['name'] = data['course']['name']
	data['alt_name'] = data['course']['alt_name']
	data['professor'] = data['course']['professor']
	del data['course']
	print data

	pass

def post_postprocessor(result=None, **kw):
	"""Accepts a single argument, `result`, which is the dictionary
	representation of the created instance of the model.

	"""
	print "COURSE------------------->POST postprocessor"
	result['course'] = result.copy()
	for key in result.keys():
		if key != 'course': 
			del result[key]

	result['course']['id'] = result['course']['courseid']
	print result	
	pass

def create_course_api(restless_manager):
	# Create API endpoints, which will be available at /api/<tablename> by
	# default. Allowed HTTP methods can be specified as well.
	restless_manager.create_api(
		Course,  
		methods=['GET', 'POST', 'DELETE', 'PUT'], 
		url_prefix='/api',
		collection_name='courses',
		postprocessors={
	        'GET_MANY': [api_get_many],
	        'POST': [post_postprocessor],
	        'PUT_SINGLE': [patch_single_postprocessor]
	    },
	    preprocessors={
	        'POST': [post_preprocessor],
	        'PUT_SINGLE': [patch_single_preprocessor]
	    }
	)