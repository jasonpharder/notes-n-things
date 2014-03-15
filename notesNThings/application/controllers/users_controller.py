from flask import Flask
from notesNThings.application.models import users_model
from notesNThings.application.models.users_model import User

import json

def api_get_many(result=None, **kw):
	print "USER: api_post_get_many"
	print result
	result['users'] = result['objects']
	for key in result.keys():
		if key != 'users': 
			del result[key]
	for test in result['users']:
		test['id'] = test['uid']
	print "after parsing:" 
	print result
	pass

def patch_single_preprocessor(instance_id=None, data=None, **kw):
	print "patch single preprocessor"
	print data
	#data = data['user'].copy()
	data['username'] = data['user']['username']
	data['password'] = data['user']['password']
	data['email'] = data['user']['email']
	data['admin'] = data['user']['admin']
	del data['user']
	print "DATA AFTER PARSING "+instance_id
	print data
	pass

def patch_single_postprocessor(result=None, **kw):
	print "patch single postprocessor"
	result['user'] = result.copy()
	for key in result.keys():
		if key != 'user': 
			del result[key]
	
	result['user']['id'] = result['user']['uid']
	print result	
	pass

def create_user_api(restless_manager):
	# Create API endpoints, which will be available at /api/<tablename> by
	# default. Allowed HTTP methods can be specified as well.
	restless_manager.create_api(
		User,  
		methods=['GET', 'POST', 'DELETE', 'PUT'], 
		url_prefix='/api',
		collection_name='users',
		postprocessors={
	        'GET_MANY': [api_get_many],
	        'GET_SINGLE': [patch_single_postprocessor],
	        'PUT_SINGLE': [patch_single_postprocessor]
	    },
	    preprocessors={
	        'PUT_SINGLE': [patch_single_preprocessor]
	    }
	)