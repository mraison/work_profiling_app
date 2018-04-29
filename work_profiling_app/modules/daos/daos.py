from ..database.userProgressPlans import \
    userSkillProgressPlan, \
    skillsMappedToSkillSet, \
    collaboratorMappedToCollabSet, \
    goalsMappedToGoalSets, \
    goals, \
    weeklySkillSetFeedBack, \
    users

from ..database.dbConnection import dbConnection


class userSkillProgressPlanDao(object):
    pass


class usersDao(dbConnection):
    def __init__(self):
        super().__init__(users)
        # Let's garentee we'll only be getting one row. Think it makes sense
        # to only be dealing with one at a time.
        # self.rowLimit = 1

    def deleteRow(self, row):
        if isinstance(row, users):
            super(usersDao, self).deleteRow(row)
        else:
            return False

    def query(self,
             userId = None,
             userName = None,
             userFullName = None,
             rowLimit = 1
    ):
        q = {}
        if userId:
            q['userId'] = userId
        if userName:
            q['userName'] = userName
        if userFullName:
            q['userName'] = userFullName

        # self.results =
        return super(usersDao, self).query(
            q,
            rowLimit
        )

    def insertRow(self, userName=None, userFullName=None):
        row = super(usersDao, self)._createNewRowInstance()
        row.userName = userName
        row.userFullName = userFullName
        super(usersDao, self).insertRow(row)
        return row



class skillsMappedToSkillSetDao(object):
    pass


class collaboratorMappedToCollabSetDao(object):
    pass

class goalsMappedToGoalSetsDao(object):
    pass

class goalsDao(object):
    pass

class weeklySkillSetFeedBackDao(object):
    pass