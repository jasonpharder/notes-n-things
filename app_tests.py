import unittest
import os
import tempfile
import sqlalchemy
from notesNThings import app, db

from notesNThings.application.models.users_model import User
from notesNThings.application.models.courses_model import Course
from notesNThings.application.models.notes_model import Note
from notesNThings.application.models.message_model import Message

TEST_DB = 'postgresql://postgres:password@localhost/notes_n_things_testdb'

class NotesTestCase(unittest.TestCase):
		def setUp(self):
				basedir = os.path.abspath(os.path.dirname(__file__))
				app.config['TESTING'] = True
				app.config['SQLALCHEMY_DATABASE_URI'] = TEST_DB
				self.app = app.test_client()
				with app.app_context():
						db.create_all()

		def tearDown(self):
				with app.app_context():
						db.session.remove()
						engine = sqlalchemy.create_engine(TEST_DB)
						metadata = sqlalchemy.MetaData(engine)
						metadata.reflect()
						metadata.drop_all()

		def testCoursesModel(self):
			with app.app_context():
				professor = User(username="Bob", password="dinosaur", email="email@email.com",
					admin = True)
				db.session.add(professor)
				db.session.flush()

				newCourse = Course(name='COMP 1010', alt_name='Computer science', professor=1)
				db.session.add(newCourse)
				db.session.flush()
				self.assertEqual(db.session.query(Course).get(1).name, 'COMP 1010')

				db.session.delete(newCourse)
				db.session.flush()

				self.assertEqual(db.session.query(Course).get(1), None)

		def testUsersModel(self):
			with app.app_context():
                                newUser = User(username="Bob", password="dinosaur", email="email@email.com",
                                        admin = False)
                                db.session.add(newUser)
                                db.session.flush()
				self.assertEqual(db.session.query(User).get(1).username, 'Bob')
				
				db.session.delete(newUser)
                                db.session.flush()

                                self.assertEqual(db.session.query(User).get(1), None)

		def testNotesModel(self):
			with app.app_context():
				notetaker = User(username="Bob", password="dinosaur", email="email@email.com",
                                        admin = False)
                                db.session.add(notetaker)
                                db.session.flush()

                                newNote = Note(uid=1, stored_as="file", file_name="lecture1", owner=1, rating=5)
                                db.session.add(newNote)
                                db.session.flush()
                                self.assertEqual(db.session.query(Note).get(1).file_name, 'lecture1')

				db.session.delete(newNote)
                                db.session.flush()

                                self.assertEqual(db.session.query(Note).get(1), None)

		def testSubscriptionRelation(self):
			with app.app_context():
				professor = User(username="Bob", password="dinosaur",
					email="email@email.com", admin = True)
				db.session.add(professor)
				db.session.flush()

				student = User(username= "Susan", password = "dinsaur",
					email = "student@email.com", admin = False)
				db.session.add(student)
				db.session.flush()

				newCourse = Course(name='COMP 1010', alt_name='Computer science',
					professor = 1)
				db.session.add(newCourse)
				db.session.flush()

				student.courses.append(newCourse)
				db.session.flush()

				self.assertEqual(len(newCourse.users), 1)
				self.assertEqual(len(student.courses), 1)

				self.assertEqual(newCourse.users.pop(), student)
				db.session.flush()

				self.assertEqual(len(newCourse.users), 0)
				self.assertEqual(len(student.courses), 0)

				newCourse.users.append(student)
				db.session.flush()

				self.assertEqual(len(newCourse.users), 1)
				self.assertEqual(len(student.courses), 1)

				self.assertEqual(newCourse.users.pop(), student)
				db.session.flush()

				self.assertEqual(len(newCourse.users), 0)
				self.assertEqual(len(student.courses), 0)

if __name__ == '__main__':
	unittest.main()
