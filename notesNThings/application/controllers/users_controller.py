from flask import Flask
from notesNThings.application.models import users_model
from notesNThings.application.models.users_model import User
import json

class UsersController:

	@staticmethod
	def getAll():
		return users_model.getAllUsers()

	@staticmethod
	def getByName(name):
		return users_model.getAllUsers()

def api_post_get_many(result=None, **kw):
	print "api_post_get_many"
	print result['objects']
	result['users'] = result['objects']
	for key in result.keys():
		#DEBUG Print
		print key 
		if key != 'users': 
			del result[key]
	for test in result['users']:
		test['id'] = test['uid']
		#DEBUG Print
		print test

def create_user_api(restless_manager):
	# Create API endpoints, which will be available at /api/<tablename> by
	# default. Allowed HTTP methods can be specified as well.
	restless_manager.create_api(
		User,  
		methods=['GET', 'POST', 'DELETE'], 
		url_prefix='/api',
		collection_name='users',
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