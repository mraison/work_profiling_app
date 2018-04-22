from database.alchemy_session import alchemy_session
from database.userProgressPlans import userNamesDB


class usersDao(object):
    def __init__(self, alchemy=None):
        if alchemy is None:
            alchemy = alchemy_session()

        self.alchemy_session = alchemy
        self.errors = []

        self._data = None


    def delete(self):
        self.alchemy_session.delete(self._data)


    def load(self, user_id=None):
        # self.results =
        q_res = self.alchemy_session.db_connection.query(userNamesDB)
        if user_id:
            q_res = q_res.filter(userNamesDB.user_id == user_id)

        self._data = q_res.all()


    def update(self, user_id=None, user_name=None):
        if user_id:
            self._data.user_id = user_id

        if user_name:
            self._data.skill_id = user_name

        self.alchemy_session.update()


    def create(self, user_id=None, user_name=None):
        row = userNamesDB()
        if user_id:
            row.user_id = user_id

        if user_name:
            row.skill_id = user_name

        self.alchemy_session.insert(row)