from ..baseController import baseController
from ...views.skills.skillsView import skillsView
from ...models.skills.skillsModel import skillsModel
from ...models.skills.skillsCollection import skillsCollection
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
                self.appSession['returnFormat'],
                {
                    'activeSkills': skills,
                    'newSkill': newSkill
                }
            )

            return view.render()
        else:
            # If we didn't get any post data then just return the usual view I think...
            return self.index()

    def skill(self, skillId):
        model = skillsModel()
        model.load(skillId=skillId)

        return render_template('skills/skill.html', version='v0.1.0', **{'skill': model})