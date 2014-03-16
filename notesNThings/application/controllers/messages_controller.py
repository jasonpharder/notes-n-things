from flask import Flask
from notesNThings.application.models.message_model import Message
import json

def api_get_many(result=None, **kw):
	print "MESSAGE: api_get_many"
	#print search_params
	print result['objects']
	result['messages'] = result['objects']
	for key in result.keys():
		print key 
		if key != 'messages': 
			del result[key]
	for test in result['messages']:
		test['id'] = test['messageid']
		print test

def api_get_many_pre(search_params=None, **kw):
	print "MESSAGE: api_get_many preprocessor"
	print search_params

def patch_single_preprocessor(instance_id=None, data=None, **kw):
	"""Accepts two arguments, `instance_id`, the primary key of the
	instance of the model to patch, and `data`, the dictionary of fields
	to change on the instance.
	"""
	print "MESSAGE------------------->patch single preprocessor"
	print data
	#data = data['user'].copy()
	data['message'] = data['message']['message']
	data['posttime'] = data['message']['postime']
	data['userid'] = data['message']['userid']
	data['courseid'] = data['message']['courseid']
	del data['message']
	print "DATA AFTER PARSING "+instance_id
	print data

def patch_single_postprocessor(result=None, **kw):
	"""Accepts a single argument, `result`, which is the dictionary
	representation of the requested instance of the model.

	"""
	print "MESSAGE------------------->patch single postprocessor"
	result['message'] = result.copy()
	for key in result.keys():
		if key != 'message': 
			del result[key]
	
	result['message']['id'] = result['message']['messageid']
	print result	
	pass

def post_preprocessor(data=None, **kw):
	"""Accepts a single argument, `data`, which is the dictionary of
	fields to set on the new instance of the model.

	"""
	print "MESSAGE------------------->POST  preprocessor"
	print data
	#data = data['user'].copy()
	data['messagetxt'] = data['message']['message']
	data['posttime'] = data['message']['posttime']
	data['userid'] = data['message']['userid']
	data['courseid'] = data['message']['courseid']

	del data['message']
	data['message'] = data['messagetxt']
	del data['messagetxt']
	print data

	pass

def post_postprocessor(result=None, **kw):
	"""Accepts a single argument, `result`, which is the dictionary
	representation of the created instance of the model.

	"""
	print "MESSAGE------------------->POST postprocessor"
	result['message'] = result.copy()
	for key in result.keys():
		if key != 'message': 
			del result[key]

	result['message']['id'] = result['message']['messageid']
	print result	
	pass

def create_message_api(restless_manager):
	# Create API endpoints, which will be available at /api/<tablename> by
	# default. Allowed HTTP methods can be specified as well.
	restless_manager.create_api(
		Message, 
		include_methods=['course', 'user'], 
		methods=['GET', 'POST', 'DELETE', 'PUT'], 
		url_prefix='/api',
		collection_name='messages',
		postprocessors={
	        'GET_MANY': [api_get_many],
	        'POST': [post_postprocessor],
	        'PUT_SINGLE': [patch_single_postprocessor]
	    },
	    preprocessors={
	    	'GET_MANY': [api_get_many_pre],
	        'POST': [post_preprocessor],
	        'PUT_SINGLE': [patch_single_preprocessor]
	    }
	)