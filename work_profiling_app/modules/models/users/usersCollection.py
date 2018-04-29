from ...daos.daos import usersDao
from ..users.usersModel import usersModel

class usersCollection(object):
    def __init__(self, dao=None):
        if not dao:
            dao = usersDao()

        self._dao = dao
        self.models = []

    def load(self, userId=None, userName=None, userFullName=None):
        rows = self._dao.query(userId, userName, userFullName, None)
        for row in rows:
            model = usersModel()
            if model.populate(row):
                self.models.append(model)