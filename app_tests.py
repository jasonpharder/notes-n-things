import os
import unittest
import tempfile
from notesNThings import app

class NotesTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(notesnthings_app.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()