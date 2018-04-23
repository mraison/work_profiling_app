from ..baseController import baseController
from ...views.users.userView import usersView
from ...daos.daos import usersDao


class usersController(baseController):
    def index(self):
        view = usersView(self.appSession['returnFormat'])
        return view.render()

    def createUser(self):
        if self.appSession['postData']['fullName']:
            fullName = self.appSession['postData']['fullName']
            dao = usersDao()
            uname = self._generate_uname(fullName)
            dao.create(uname, fullName)

            view = usersView(
                self.appSession['returnFormat'],
                userId=dao.row.data.userId,
                userFullName=dao.row.data.userFullName,
                userName=dao.row.data.userName
            )

            return view.render()

    def _generate_uname(self, fullName):
        fullNameA = fullName.split()
        if len(fullNameA):
            return fullName
        else:
            return fullNameA[0][0] + fullNameA[1]


