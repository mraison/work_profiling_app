from ...daos.daos import skillsDao, skillsMappedToSkillSetDao
from ..skills.skillsModel import skillsModel

class skillsCollection(object):
    def __init__(self, dao=None, skillSetDao=None):
        if not dao:
            dao = skillsDao()

        if not skillSetDao:
            skillSetDao = skillsMappedToSkillSetDao()

        self._dao = dao
        self._skillSetDao = skillSetDao
        self._skillSetId = None
        self.models = []
        self.skillSet = []

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

    def loadSkillSet(self,
                     skillSetId=None,
                     skillSetName=None
                     ):
        self.skillSet = self._skillSetDao.query(skillSetId, skillSetName)
        if self.skillSet:
            self._skillSetId = self.skillSet[0].skillSetId

        for row in self.skillSet:
            skillRow = skillsModel()
            skillRow.load(row.skillId)
            if skillRow:
                self.models.append(skillRow)

    def saveSkillSet(self,
                     skillSetName
                       ):
        for skill in self.models:
            if skill.data.skillId:
                newRow = self._skillSetDao.insertRow(skillSetName, skill.data.skillId, self._skillSetId)
                self.skillSet.append(newRow)
                if newRow and not self._skillSetId:
                    self._skillSetId = newRow.skillSetId



