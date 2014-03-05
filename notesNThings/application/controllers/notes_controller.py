from flask import Flask
from notesNThings.application.models import notes_model
import json

class NotesController:

	@staticmethod
	def getAll():
		return notes_model.getAllNotes()

	@staticmethod
	def getByName(name):
		return notes_model.getAllNotes()