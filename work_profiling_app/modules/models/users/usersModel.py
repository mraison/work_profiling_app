from ...daos.daos import usersDao
from ...database.userProgressPlans import users

class usersModel(object):
    def __init__(self, dao=None):
        if not dao:
            dao = usersDao()

        self._dao = dao
        self._dao.rowLimit = 1

        self.data=None

    def load(self, userId=None, userName=None, userFullName=None):
        self.data = self._dao.query(userId, userName, userFullName, 1)

    def createNewUser(self, userName, userFullName):
        self.data = self._dao.insertRow(userName, userFullName)

    def delete(self):
        if self.data:
            self._dao.deleteRow(self.data)
            self.data = None
            return True
        else:
            return False

    def update(self, userName, userFullName):
        # a couple things to keep in mind here...user's shouldn't be able to update their userId
        # both the new userName and the full Name must be provided. they are derivations of eachother after all.
        if self.data:
            self.data.userName = userName
            self.data.userFullName = userFullName
            self.data.commit()
            return True
        else:
            return False

    def populate(self, row):
        # here we assume that the row is a users database object. we'll place it in data
        if isinstance(row, users):
            self.data = row
            return True
        else:
            return False


    def getUserId(self):
        if not self.data:
            return self.data.userId
        else:
            return None

    def getUserName(self):
        if self.data:
            return self.data.userName
        else:
            return None

    def getUserFullName(self):
        if self.data:
            return self.data.userFullName
        else:
            return None


