from database.db_connections import profilesDB
from work_profiling_app.modules.daos.alchemy_session import alchemy_session

class profilesDao(object):
    def __init__(self, alchemy=None):
        if alchemy is None:
            alchemy = alchemy_session()

        self.alchemy_session = alchemy
        self.errors = []

        self.user_id = None
        self.skill_id = None
        self.collab_id = None
        self.week_id = None
        # self.feedback = None  Shouldn't include this since it's not a key. it's the value we want.

        self._data = None

    def delete(self):
        self.alchemy_session.delete(self._data)

    def load(self,
             user_id=None,
             skill_id=None,
             collab_id=None,
             week_id=None
    ):
        # self.results =
        q_res = self.alchemy_session.db_connection.query(profilesDB)
        if user_id:
            q_res.filter(profilesDB.user_id == self.user_id)

        if skill_id:
            q_res.filter(profilesDB.skill_id == self.skill_id)

        if collab_id:
            q_res.filter(profilesDB.collab_id == self.collab_id)

        if week_id:
            q_res.filter(profilesDB.week_id == self.week_id)

        self._data = q_res.first()

    def update(self,
            user_id=None,
            skill_id=None,
            collab_id=None,
            week_id=None,
            feedback=None
    ):
        if user_id:
            self._data.user_id = user_id

        if skill_id:
            self._data.skill_id = skill_id

        if collab_id:
            self._data.collab_id = collab_id

        if week_id:
            self._data.week_id = week_id

        if feedback:
            self._data.feedback = feedback

        self.alchemy_session.update()


    def create(self,
        user_id=None,
        skill_id=None,
        collab_id=None,
        week_id=None,
        feedback=None
    ):
        row = profilesDB()
        if user_id:
            row.user_id = user_id

        if skill_id:
            row.skill_id = skill_id

        if collab_id:
            row.collab_id = collab_id

        if week_id:
            row.week_id = week_id

        if feedback:
            row.feedback = feedback

        self.alchemy_session.insert(row)