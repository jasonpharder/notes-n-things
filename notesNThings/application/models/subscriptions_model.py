from notesNThings.application.models import db
from sqlalchemy import Table, Column, Integer, ForeignKey, UniqueConstraint

subscriptionTable = Table(
    'association',
    db.Model.metadata,
    Column('userID', Integer, ForeignKey('users.uid')),
    Column('courseID', Integer, ForeignKey('courses.courseid')),
    UniqueConstraint('userID', 'courseID')
)
