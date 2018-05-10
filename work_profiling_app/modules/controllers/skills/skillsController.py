from ..baseController import baseController
from ...views.skills.skillsView import skillsView
from ...models.skills.skillsModel import skillsModel
from ...models.skills.skillsCollection import skillsCollection
from ...models.skills.skillSet import skillSet
from flask import render_template

class skillsController(baseController):
    def index(self):
        skills = skillsCollection()
        skills.load()

        view = skillsView(self.appSession['returnFormat'], {'activeSkills': skills})
        return view.render()

    def createSkills(self):
        if self.appSession['postData']['skillName'] and self.appSession['postData']['skillDescription']:
            skillName = self.appSession['postData']['skillName']
            skillDescription = self.appSession['postData']['skillDescription']
            newSkill = skillsModel()

            newSkill.createNewSkill(skillName, skillDescription)

            skills = skillsCollection()
            skills.load()

            view = skillsView(
                # self.appSession['returnFormat'],
                'json',
                 {
                    'newSkill': newSkill
                 }
            )

            return view.render()
        else:
            # If we didn't get any post data then just return the usual view I think...
            return self.index()

    def createSkillSets(self):
        if self.appSession['postData']['skillSetName'] and self.appSession['postData']['skillIds']:
            skillSetName = self.appSession['postData']['skillSetName']
            skillIds = self.appSession['postData']['skillIds']
            newSkillSet = skillSet()
            newSkillSet.skillIds = skillIds
            newSkillSet.skillSetName = skillSetName
            newSkillSet.saveNew()

            view = skillsView(
                self.appSession['returnFormat'],
                {
                    'activeSkillSet': skills,
                    'newSkillSet': newSkillSet
                }
            )
            return view.render()
        else:
            return self.index()


    def skill(self, skillId):
        model = skillsModel()
        model.load(skillId=skillId)

        return render_template('skills/skill.html', version='v0.1.0', **{'skill': model})