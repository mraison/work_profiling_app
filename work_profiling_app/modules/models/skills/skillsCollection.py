from ...daos.daos import skillsDao
from ..skills.skillsModel import skillsModel

class skillsCollection(object):
    def __init__(self, dao=None):
        if not dao:
            dao = skillsDao()

        self._dao = dao
        self.models = []

    def load(self,
             skillId=None,
             skillName=None,
             skillDescription=None
             ):
        rows = self._dao.query(skillId, skillName, skillDescription, None)
        for row in rows:
            model = skillsModel()
            if model.populate(row):
                self.models.append(model)