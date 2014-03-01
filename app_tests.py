import os
import unittest
import tempfile
from notesNThings import notesnthings_app

class NotesTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, notesnthings_app.app.config['DATABASE'] = tempfile.mkstemp()
        notesnthings_app.app.config['TESTING'] = True
        self.app = notesnthings_app.app.test_client()
        notesnthings_app.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(notesnthings_app.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()