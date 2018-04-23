from ..baseController import baseController
from ...views.users.userView import usersView

class usersController(baseController):
    def index(self):
        view = usersView(self.appSession['returnFormat'])
        return view.render()

    def createUser(self, name):
