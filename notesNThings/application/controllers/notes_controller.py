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

def create_note_api(restless_manager):
	# Create API endpoints, which will be available at /api/<tablename> by
	# default. Allowed HTTP methods can be specified as well.
	restless_manager.create_api(
		Note,  
		methods=['GET', 'POST', 'DELETE'], 
		url_prefix='/api',
		collection_name='notes',
		postprocessors={
	        'GET_MANY': [api_post_get_many]
	        #'POST': [api_post_get_many],
	        #'PUT_SINGLE': [api_post_get_many]
	    },
	    preprocessors={
	        #'POST': [api_post_get_many],
	        #'PUT_SINGLE': [api_post_get_many]
	    }
	)