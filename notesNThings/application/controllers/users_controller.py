from flask import Flask
from notesNThings.application.models import users_model
import json

class NotesController:

	@staticmethod
	def getAll():
		return json.dumps(stubNotes)

	@staticmethod
	def getByName(name):
		return json.dumps(stubNote)