from ..baseController import baseController
from ...views.users.userView import usersView
from ...daos.daos import usersDao

from ...database.dbConnection import dbRow

class usersController(baseController):
    def index(self):
        usersd = usersDao()
        usersd.rowLimit = None
        usersd.load()
        if usersd.row is None:
            userMod = []
        elif isinstance(usersd.row, dbRow):
            userMod = [usersd.row]
        else:
            userMod = usersd.row.rows

        view = usersView(self.appSession['returnFormat'], {'activeUsers': userMod})
        return view.render()

    def createUser(self):
        if self.appSession['postData']['fullName']:
            fullName = self.appSession['postData']['fullName']
            dao = usersDao()

            uname = self._generate_uname(fullName)
            dao.create(uname, fullName)

            dao.rowLimit = None
            dao.load()
            if dao.row is None:
                userMod = []
            elif isinstance(dao.row, dbRow):
                userMod = [dao.row]
            else:
                userMod = dao.row

            view = usersView(
                self.appSession['returnFormat'],
                {
                    'userId': dao.row.data.userId,
                    'userFullName': dao.row.data.userFullName,
                    'userName': dao.row.data.userName,
                    'activeUsers': userMod
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


