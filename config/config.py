import os
basedir = os.path.abspath(os.path.dirname(__file__))

DB_DIALECT = 'postgresql'
DB_DRIVER  = '' #If a dirver is defined this sting must be of the format '+diver'
DB_USER    = 'notes'
DB_PASS    = 'testpasspleaseignore'
DB_HOST    = 'localhost'
DB_DB      = 'notes-n-things'

SQLALCHEMY_DATABASE_URI = DB_DIALECT+DB_DRIVER+'://'+DB_USER+':'+DB_PASS+'@'+DB_HOST+'/'+DB_DB
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')