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

    def newRow(self):
        row = dbRow(self.dbConnection, True, self.dbObj())
        return row

    def loadRows(self, queries={}, limit = None):
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

        if len(data) == 1:
            return dbRows(dbRow(self.dbConnection, False, data[0]))
        elif len(data) == 0:
            return False
        else:
            return dbRows([dbRow(self.dbConnection, False, d) for d in data])


class dbRow(object):

    def __init__(self, dbConnection, _isNew = True, _data = None):
        self._dbConnection = dbConnection
        self._isNew = _isNew
        self.data = _data

    def commit(self):
        if not self.data:
            return False

        if self._isNew:
            self._dbConnection.add(self.data)
            self._isNew = False

        self._dbConnection.commit()
        return True

    def delete(self):
        self._dbConnection.delete(self.data)
        self._dbConnection.commit()
        self.data = None
        return True


class dbRows(object):
    def __init__(self, rows=[]):
        self.rows = rows # expect these to be of type dbRow

    def addRow(self, row):
        # expect row to be instance of dbRow
        self.rows.append(row)

    def addRows(self, rows):
        # expect rows to be instance of dbRows
        for row in rows.rows:
            self.addRow(row)

    def drop(self, rowIndex):
        if self.rows[rowIndex]:
            del self.rows[rowIndex]

    def commitAll(self):
        if not self.rows:
            return False

        for row in self.rows:
            row.commit()

        return True

    def deleteAll(self):
        if not self.rows:
            return False

        for row in self.rows:
            row.delete()

        self.rows = []
        return True

    def count(self):
        return len(self.rows)

    def getFirst(self):
        if self.rows[0]:
            return self.rows[0]


class dbScheme(object):
    def __init__(self, db):
        self._scheme = [key for key, value in db.__dict__.items() if
         type(value) == InstrumentedAttribute]

    def getBlankRowScheme(self):
        return {key: None for key in self._scheme}