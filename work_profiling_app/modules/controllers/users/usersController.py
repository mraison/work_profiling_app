from ..baseController import baseController
from ...views.users.userView import usersView
from ...models.users.usersModel import usersModel
from ...models.users.usersCollection import usersCollection
from flask import render_template

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

            newUser.createNewSkill(uname, fullName)

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

    def user(self, userId):
        model = usersModel()
        model.load(userId=userId)

        return render_template('users/user.html', version='v0.1.0', **{'user': model})

    def _generate_uname(self, fullName):
        fullNameA = fullName.lower().split()
        if len(fullNameA) == 1:
            return fullName
        else:
            return fullNameA[0][0] + fullNameA[1]


