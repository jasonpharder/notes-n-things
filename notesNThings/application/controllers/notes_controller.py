from flask import Flask
from notesNThings.application.models import notes_model
from notesNThings.application.models.notes_model import Note
import json

class NotesController:

	@staticmethod
	def getAll():
		return notes_model.getAllNotes()

	@staticmethod
	def getByName(name):
		return notes_model.getAllNotes()

def api_post_get_many(result=None, **kw):
	print "NOTE: api_post_get_many"
	print result['objects']
	result['notes'] = result['objects']
	for key in result.keys():
		#DEBUG Print
		print key 
		if key != 'notes': 
			del result[key]
	for test in result['notes']:
		test['id'] = test['uid']
		#DEBUG Print
		print test

def post_preprocessor(data=None, **kw):
	"""Accepts a single argument, `data`, which is the dictionary of
	fields to set on the new instance of the model.

	"""
	print "NOTE------------------->POST  preprocessor"
	print data

	data['stored_as'] = data['note']['stored_as']
	data['owner'] = data['note']['owner']
	del data['note']
	print data

	pass

def post_postprocessor(result=None, **kw):
	"""Accepts a single argument, `result`, which is the dictionary
	representation of the created instance of the model.

	"""
	print "NOTE------------------->POST postprocessor"
	result['note'] = result.copy()
	for key in result.keys():
		if key != 'note': 
			del result[key]

	result['note']['id'] = result['note']['uid']
	print result	
	pass

def create_note_api(restless_manager):
	# Create API endpoints, which will be available at /api/<tablename> by
	# default. Allowed HTTP methods can be specified as well.
	restless_manager.create_api(
		Note,  
		methods=['GET', 'POST', 'DELETE'], 
		url_prefix='/api',
		collection_name='notes',
		postprocessors={
	        'GET_MANY': [api_post_get_many],
	        'POST': [post_postprocessor],
	        #'PUT_SINGLE': [api_post_get_many]
	    },
	    preprocessors={
	        'POST': [post_preprocessor],
	        #'PUT_SINGLE': [api_post_get_many]
	    }
	)
