from work_profiling_app.modules.daos.daos import usersDao


class usersModel(object):
    def __init__(self, dao=None):
        if not dao:
            dao = usersDao()

        self._dao = dao
        self._dao.rowLimit = 1


    def create(self, uname, fullName):
        self._dao.create(uname, fullName)