from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.userProgressPlans import Base

class alchemy_session:

    def __init__(self):
        engine = create_engine('sqlite:///userProgressPlans.db')
        # Bind the engine to the metadata of the Base class so that the
        # declaratives can be accessed through a DBSession instance
        Base.metadata.bind = engine

        DBSession = sessionmaker(bind=engine)
        # A DBSession() instance establishes all conversations with the database
        # and represents a "staging zone" for all the objects loaded into the
        # database session object. Any change made against the objects in the
        # session won't be persisted into the database until you call
        # session.commit(). If you're not happy about the changes, you can
        # revert all of them back to the last commit by calling
        # session.rollback()
        self.db_connection = DBSession()

        self._dbScheme = None # a scheme for the database to conform to.

        self.errors = []

        self._data = None


    def insert(self, rows):
        self.db_connection.add(row)
        self.db_connection.commit()


    def delete(self, rows):
        self.db_connection.delete(row)
        self.db_connection.commit()


    def update(self, row):
        self.db_connection.commit()

