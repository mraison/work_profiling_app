from .skillsCollection import skillsCollection
from ...daos.daos import skillsMappedToSkillSetDao


## @todo: convert this into a model that has a skill collection as a variable.
class skillSetModel(object):
    def __init__(self, skillDao=None, skillSetDao=None):
        if not skillSetDao:
            skillSetDao = skillsMappedToSkillSetDao()

        self.skills = skillsCollection(skillDao)
        self._dao = skillSetDao

        self.skillIds = None
        self.skillSetName = None
        self.skillSetId = None

        self.data = None

    def load(self,
             skillSetId=None,
             skillSetName=None
             ):
        self.data = self._dao.query(skillSetId, skillSetName)
        self.skillSetName = self.data.skillSetName
        self.skillIds = self.data.skillIds
        self.skillSetId = self.data.skillSetId

        if self.skillIds:
            skillIdList = self.skillIds.split(',')
            for skillId in skillIdList:
                self.skills.load(skillId)

    def addSkill(self,
                 skillId
            ):
        if self.skillIds and skillId not in self.skillIds:
            self.skills.load(skillId)
            self.skillIds+=str(',' + skillId)

    def removeSkillFromSet(self,
                           skillId
                           ):
        ## remove from the collection of skills we got.
        for index, skill in enumerate(self.skills.models):
            if skillId == skill.data.skillId:
                del self.skills.models[index]
                break


    def saveNew(self):
        if self.skillSetName and self.skillIds:
            self.data = self._dao.insertRow(self.skillSetName, self.skillIds)
            self.skillSetId = self.data.skillSetId

    def update(self,
               skillSetName=None
               ):
        if self.data:
            self.data.skillIds = self.skillIds
            if skillSetName:
                self.data.skillSetName = skillSetName
            self.data.commit()
            return True
        else:
            return False

    def removeSet(self):
        if self.data:
            self._dao.deleteRow(self.data)
            self.data = None
            return True
        else:
            return False
