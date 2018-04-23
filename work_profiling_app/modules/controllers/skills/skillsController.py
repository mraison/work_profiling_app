from ..baseController import baseController
from ...views.skills.skillsView import skillsView


class skillsController(baseController):
    def index(self):
        view = skillsView(self.appSession['returnFormat'])
        return view.render()