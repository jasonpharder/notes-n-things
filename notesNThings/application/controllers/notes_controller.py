from flask import Flask
import json

class NotesController:
	
	@staticmethod
	def getAll():
		stubNotes = { 'notes': [ {'id' : 0, 'noteID': '0', "file_name": "someFile", "contents": "test content please ignore"}, { 'id': 1,  "noteID": '1', "file_name": "myOtherFile", "contents": "the other test content"} ]}
		return json.dumps(stubNotes)

	@staticmethod
	def getByName(name):
		stubNote =  { 'notes': [ {'id': '0', 'noteID': '0', "file_name": "someFile", "contents": "test content please ignore"} ]}
		return json.dumps(stubNote)
