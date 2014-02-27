from flask import Flask
import json

class NotesController:
	
	@staticmethod
	def getAll():
		stubNotes = [ {'noteID': 0, 'stored_as': "placeholder data", "file_name": "someFile", "owner": None, "rating": 4}, {"noteID": 1, "stored_as": "placeholder data", "file_name": "myOtherFile", "owner": None, "rating": 5} ]
		return json.dumps(stubNotes)

	@staticmethod
	def getByName(name):
		stubNote = {'noteID': 0, 'stored_as': "placeholder data", "file_name": "someFile", "owner": None, "rating": 4}
		return json.dumps(stubNote)
