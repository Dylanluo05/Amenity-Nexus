""" database dependencies to support Users db examples """

from __init__ import db
from sqlalchemy.exc import IntegrityError
# from flask_login import UserMixin

''' Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along '''


# Define the 'Users Notes' table  with a relationship to Users within the model
# Relationships are expressed with the relationship() function. However the foreign key has to be separately declared with the ForeignKey class.
# A Foreign key is a column that creates a relationship between two tables. The purpose of the Foreign key is to maintain data integrity and allow navigation between two different instances of an entity. It acts as a cross-reference between two tables as it references the primary key of another table(Users in our case). Every relationship in the database should be supported by a foreign key.

class Phonebook(db.Model):
    __tablename__ = 'phonebook'

    # Define the Notes schema
    id = db.Column(db.Integer, primary_key=True)
    servicephonenumber1 = db.Column(db.Text, unique=False, nullable=False)
    servicephonenumber2 = db.Column(db.Text, unique=False, nullable=False)
    servicephonenumber3 = db.Column(db.Text, unique=False, nullable=False)
    servicephonenumber4 = db.Column(db.Text, unique=False, nullable=False)
    servicephonenumber5 = db.Column(db.Text, unique=False, nullable=False)
    servicephonenumber6 = db.Column(db.Text, unique=False, nullable=False)
    servicephonenumber7 = db.Column(db.Text, unique=False, nullable=False)
    servicephonenumber8 = db.Column(db.Text, unique=False, nullable=False)
    servicephonenumber9 = db.Column(db.Text, unique=False, nullable=False)
    servicephonenumber10 = db.Column(db.Text, unique=False, nullable=False)
    servicephonenumber11 = db.Column(db.Text, unique=False, nullable=False)
    servicephonenumber12 = db.Column(db.Text, unique=False, nullable=False)
    servicephonenumber13 = db.Column(db.Text, unique=False, nullable=False)
    servicephonenumber14 = db.Column(db.Text, unique=False, nullable=False)
    servicephonenumber15 = db.Column(db.Text, unique=False, nullable=False)
    servicephonenumber16 = db.Column(db.Text, unique=False, nullable=False)
    servicephonenumber17 = db.Column(db.Text, unique=False, nullable=False)
    servicephonenumber18 = db.Column(db.Text, unique=False, nullable=False)
    servicephonenumber19 = db.Column(db.Text, unique=False, nullable=False)
    servicephonenumber20 = db.Column(db.Text, unique=False, nullable=False)
    servicephonenumber21 = db.Column(db.Text, unique=False, nullable=False)

    userID = db.Column(db.Integer, db.ForeignKey('users.userID'))

    # Constructor of a Notes object, initializes of instance variables within object
    def __init__(self, servicephonenumber1, servicephonenumber2, servicephonenumber3, servicephonenumber4,
                 servicephonenumber5, servicephonenumber6, servicephonenumber7, servicephonenumber8,
                 servicephonenumber9, servicephonenumber10, servicephonenumber11, servicephonenumber12,
                 servicephonenumber13, servicephonenumber14, servicephonenumber15, servicephonenumber16,
                 servicephonenumber17, servicephonenumber18, servicephonenumber19, servicephonenumber20,
                 servicephonenumber21, userID):
        self.servicephonenumber1 = servicephonenumber1
        self.servicephonenumber2 = servicephonenumber2
        self.servicephonenumber3 = servicephonenumber3
        self.servicephonenumber4 = servicephonenumber4
        self.servicephonenumber5 = servicephonenumber5
        self.servicephonenumber6 = servicephonenumber6
        self.servicephonenumber7 = servicephonenumber7
        self.servicephonenumber8 = servicephonenumber8
        self.servicephonenumber9 = servicephonenumber9
        self.servicephonenumber10 = servicephonenumber10
        self.servicephonenumber11 = servicephonenumber11
        self.servicephonenumber12 = servicephonenumber12
        self.servicephonenumber13 = servicephonenumber13
        self.servicephonenumber14 = servicephonenumber14
        self.servicephonenumber15 = servicephonenumber15
        self.servicephonenumber16 = servicephonenumber16
        self.servicephonenumber17 = servicephonenumber17
        self.servicephonenumber18 = servicephonenumber18
        self.servicephonenumber19 = servicephonenumber19
        self.servicephonenumber20 = servicephonenumber20
        self.servicephonenumber21 = servicephonenumber21
        self.userID = userID

    # Returns a string representation of the Notes object, similar to java toString()
    # returns string
    def __repr__(self):
        return "Personalization(" + str(self.id) + "," + self.servicephonenumber1 + "," + self.servicephonenumber2 + "," + \
               self.servicephonenumber3 + "," + self.servicephonenumber4 + "," + self.servicephonenumber5 + "," + self.servicephonenumber6 + "," + \
               self.servicephonenumber7 + "," + self.servicephonenumber8 + "," + self.servicephonenumber9 + "," + self.servicephonenumber10 + "," + \
               self.servicephonenumber11 + "," + self.servicephonenumber12 + "," + self.servicephonenumber13 + "," + self.servicephonenumber14 + "," + \
               self.servicephonenumber15 + "," + self.servicephonenumber16 + "," + self.servicephonenumber17 + "," + self.servicephonenumber18 + "," + \
               self.servicephonenumber19 + "," + self.servicephonenumber20 + "," + self.servicephonenumber21 + "," + str(self.userID) + ")"

    # CRUD create, adds a new record to the Notes table
    # returns the object added or None in case of an error
    def create(self):
        try:
            # creates a Notes object from Notes(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Notes table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read, returns dictionary representation of Notes object
    # returns dictionary
    def read(self):
        return {
            "id": self.id,
            "servicephonenumber1": self.servicephonenumber1,
            "servicephonenumber2": self.servicephonenumber2,
            "servicephonenumber3": self.servicephonenumber3,
            "servicephonenumber4": self.servicephonenumber4,
            "servicephonenumber5": self.servicephonenumber5,
            "servicephonenumber6": self.servicephonenumber6,
            "servicephonenumber7": self.servicephonenumber7,
            "servicephonenumber8": self.servicephonenumber8,
            "servicephonenumber9": self.servicephonenumber9,
            "servicephonenumber10": self.servicephonenumber10,
            "servicephonenumber11": self.servicephonenumber11,
            "servicephonenumber12": self.servicephonenumber12,
            "servicephonenumber13": self.servicephonenumber13,
            "servicephonenumber14": self.servicephonenumber14,
            "servicephonenumber15": self.servicephonenumber15,
            "servicephonenumber16": self.servicephonenumber16,
            "servicephonenumber17": self.servicephonenumber17,
            "servicephonenumber18": self.servicephonenumber18,
            "servicephonenumber19": self.servicephonenumber19,
            "servicephonenumber20": self.servicephonenumber20,
            "servicephonenumber21": self.servicephonenumber21,

            "userID": self.userID,
        }

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None

# Define the Users table within the model
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) Users represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL