from ..database.userProgressPlans import \
    userSkillProgressPlan, \
    skillsMappedToSkillSet, \
    collaboratorMappedToCollabSet, \
    goalsMappedToGoalSets, \
    goals, \
    weeklySkillSetFeedBack, \
    users

from ..database.dbConnection import dbConnection

class usersDao(object):
    def __init__(self):
        super().__init__(users)
        # Let's garentee we'll only be getting one row. Think it makes sense
        # to only be dealing with one at a time.
        self.rowLimit = 1

    def __init__(self, dbObj=None):
        if dbObj is None:
            dbObj = users

        self.dbConnection = dbConnection(dbObj)
        self.row = None
        # Let's garentee we'll only be getting one row. Think it makes sense
        # to only be dealing with one at a time.
        self.rowLimit = 1
