from database.alchemy_session import alchemy_session
from database.db_connections import skillDescriptionsDB


class skillsDao(object):
    def __init__(self, alchemy=None):
        if alchemy is None:
            alchemy = alchemy_session()

        self.alchemy_session = alchemy
        self.errors = []

        self._data = None


    def delete(self):
        self.alchemy_session.delete(self._data)


    def load(self, skill_id=None):
        # self.results =
        q_res = self.alchemy_session.db_connection.query(skillDescriptionsDB)
        if skill_id:
            q_res = q_res.filter(skillDescriptionsDB.skill_id == skill_id)

        self._data = q_res.all()


    def update(self, skill_id=None, skill_description=None):
        if skill_id:
            self._data.skill_id = skill_id

        if skill_description:
            self._data.skill_description = skill_description

        self.alchemy_session.update()


    def create(self, skill_id=None, skill_description=None):
        row = skillDescriptionsDB()
        if skill_id:
            row.skill_id = skill_id

        if skill_description:
            row.skill_description = skill_description

        self.alchemy_session.insert(row)