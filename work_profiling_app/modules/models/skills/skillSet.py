from skillsCollection import skillsCollection
from ...daos.daos import skillsMappedToSkillSetDao


## @todo: convert this into a model that has a skill collection as a variable.
class skillSet(skillsCollection):
    def __init__(self, skillDao=None, skillSetDao=None):
        super().__init__(skillDao)

        if not skillSetDao:
            skillSetDao = skillsMappedToSkillSetDao()

        self.skillSetDao = skillSetDao
        self.skillIds = None
        self.skillSetName = None

    def load(self,
             skillSetId=None,
             skillSetName=None
             ):
        self.skillSetData = self.skillSetDao.query(skillSetId, skillSetName)
        self.skillSetName = self.skillSetData.skillSetName
        self.skillIds = self.skillSetData.skillIds
        self.skillSetId = self.skillSetData.skillSetId

        if self.skillIds:
            skillIdList = self.skillIds.split(',')
            for skillId in skillIdList:
                super(skillSet, self).load(skillId)

    def addSkill(self,
                 skillId
            ):
        if self.skillIds and skillId not in self.skillIds:
            super(skillSet, self).load(skillId)
            self.skillIds+=str(',' + skillId)

    def saveNew(self,
             skillSetName
             ):
        self.skillSetDao.insertRow(skillSetName, self.skillIds)

    def update(self,
               skillSetName=None
               ):
        if self.skillSetData:
            self.skillSetData.skillIds = self.skillIds
            if skillSetName:
                self.skillSetData.skillSetName = skillSetName
            self.skillSetData.commit()
            return True
        else:
            return False

    def removeSet(self):
        if self.skillSetData:
            self.skillSetDao.deleteRow(self.skillSetData)
            self.skillSetData = None
            return True
        else:
            return False

