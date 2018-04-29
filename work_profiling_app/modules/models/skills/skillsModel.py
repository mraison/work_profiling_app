from ...daos.daos import skillsDao
from ...database.userProgressPlans import skills

class skillsModel(object):
    def __init__(self, dao=None):
        if not dao:
            dao = skillsDao()

        self._dao = dao
        self._dao.rowLimit = 1

        self.data=None

    def load(self,
             skillId=None,
             skillName=None,
             skillDescription=None
             ):
        self.data = self._dao.query(skillId, skillName, skillDescription, 1)

    def createNewSkill(self,
                       skillName=None,
                       skillDescription=None
                       ):
        self.data = self._dao.insertRow(skillName, skillDescription)

    def delete(self):
        if self.data:
            self._dao.deleteRow(self.data)
            self.data = None
            return True
        else:
            return False

    def update(self,
               skillName=None,
               skillDescription=None
               ):
        # a couple things to keep in mind here...user's shouldn't be able to update their userId
        # both the new userName and the full Name must be provided. they are derivations of eachother after all.
        if self.data:
            self.data.skillName = skillName
            self.data.skillDescription = skillDescription
            self.data.commit()
            return True
        else:
            return False

    def populate(self, row):
        # here we assume that the row is a users database object. we'll place it in data
        if isinstance(row, skills):
            self.data = row
            return True
        else:
            return False


    def getSkillId(self):
        if not self.data:
            return self.data.skillId
        else:
            return None

    def getSkillName(self):
        if self.data:
            return self.data.skillName
        else:
            return None

    def getSkillDescription(self):
        if self.data:
            return self.data.skillDescription
        else:
            return None


