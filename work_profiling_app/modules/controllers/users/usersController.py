from ..baseController import baseController
from ...views.users.userView import usersView
from ...models.users.usersModel import usersModel
from ...models.users.usersCollection import usersCollection

class usersController(baseController):
    def index(self):
        users = usersCollection()
        users.load()

        view = usersView(self.appSession['returnFormat'], {'activeUsers': users})
        return view.render()

    def createUser(self):
        if self.appSession['postData']['fullName']:
            fullName = self.appSession['postData']['fullName']
            uname = self._generate_uname(fullName)
            newUser = usersModel()

            newUser.createNewUser(uname, fullName)

            users = usersCollection()
            users.load()

            view = usersView(
                self.appSession['returnFormat'],
                {
                    'activeUsers': users,
                    'newUser': newUser
                }
            )

            return view.render()
        else:
            # If we didn't get any post data then just return the usual view I think...
            return self.index()

    def _generate_uname(self, fullName):
        fullNameA = fullName.lower().split()
        if len(fullNameA) == 1:
            return fullName
        else:
            return fullNameA[0][0] + fullNameA[1]


