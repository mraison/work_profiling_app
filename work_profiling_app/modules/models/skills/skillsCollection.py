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
        if not rows:
            return False

        for row in rows:
            model = skillsModel()
            if model.populate(row):
                self.models.append(model)

        return True


