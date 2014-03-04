from flask import Flask
from notesNThings.application.models import users_model
import json

class UsersController:

	@staticmethod
	def getAll():
		return users_model.getAllUsers()

	@staticmethod
	def getByName(name):
		return users_model.getAllUsers()