from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.attributes import InstrumentedAttribute

from .userProgressPlans import Base


class dbConnection(object):

    def __init__(self, dbObj):
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
        self.dbConnection = DBSession()

        # this probably isn't a greate idea because I'd need to keep this up to date with the userProgressPlan file...
        # but I really just need a quick list of these somewhere.
        self._dbList = [
            'userSkillProgressPlan',
            'skillsMappedToSkillSet',
            'collaboratorMappedToCollabSet',
            'goalsMappedToGoalSets',
            'goals',
            'weeklySkillSetFeedBack'
        ]

        self.dbObj = dbObj

        self.errors = []

    def insertRow(self, row):
        # assume row is instance of whatever dbObj is.
        self.dbConnection.add(row)
        self.dbConnection.commit()

    def insertRows(self, rows):
        for r in rows:
            self.dbConnection.add(r)

        self.dbConnection.commit()

    def query(self, queries={}, limit = None):
        qRes = self.dbConnection.query(self.dbObj)

        # apply queries
        for key, value in queries.items():
            if not value:
                # skip over null values
                continue

            if hasattr(self.dbObj, key):
                a = getattr(self.dbObj, key)
                qRes.filter(a == value)
            else:
                self.errors.append('Column %r not found in db %r. This filter will be ignored' % (key, self.dbObj.__name__))

        # apply limit
        if limit:
            data = qRes.limit(limit)
        else:
            data = qRes.all()

        return data

    def deleteRow(self, row):
        # assume row is instance of whatever dbObj is.
        self.dbConnection.delete(self.data)
        self.dbConnection.commit()

    def deleteRows(self, rows):
        for r in rows:
            self.dbConnection.delete(r)

        self.dbConnection.commit()

    def _createNewRowInstance(self):
        return self.dbObj()


class dbScheme(object):
    def __init__(self, db):
        self._scheme = [key for key, value in db.__dict__.items() if
         type(value) == InstrumentedAttribute]

    def getBlankRowScheme(self):
        return {key: None for key in self._scheme}