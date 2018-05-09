from ...baseController import baseController
from ....models.skills.skillsCollection import skillsCollection
from ....daos.daos import skillsMappedToSkillSetDao

class skillSetController(baseController):
    def index(self):
        dao = skillsMappedToSkillSetDao()
        qRes = dao.query(None, None, None)
        skillset = [r.skillSetName for r in qRes]
        skillsetUnique = set(skillset)

        skills = skillsCollection()
        skills.loadSkillSet()


        view = skillsView(self.appSession['returnFormat'], {'activeSkills': skills})
        return view.render()