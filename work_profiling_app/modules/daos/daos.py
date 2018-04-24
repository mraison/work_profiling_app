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
    def __init__(self, dbObj=None):
        if dbObj is None:
            dbObj = userSkillProgressPlan

        self.dbConnection = dbConnection(dbObj)
        self.row = None
        # Let's garentee we'll only be getting one row. Think it makes sense
        # to only be dealing with one at a time.
        self.rowLimit = 1

    def delete(self):
        if self.row:
            self.row.delet()

    def load(self,
             userId=None,
             skillSetId=None,
             collabSetId=None,
             goalSetId=None
    ):
        # self.results =
        self.row = self.dbConnection.loadRows(
            {
                'userId': userId,
                'skillSetId': skillSetId,
                'collabSetId': collabSetId,
                'goalSetId': goalSetId
            },
            self.rowLimit
        )

    def update(self,
               userId=None,
               skillSetId=None,
               collabSetId=None,
               goalSetId=None
    ):
        if userId:
            self.row._data.userId = userId

        if skillSetId:
            self.row._data.skillSetId = skillSetId

        if collabSetId:
            self.row._data.collabSetId = collabSetId

        if goalSetId:
            self.row._data.goalSetId = goalSetId

        self.row.commit()

    def create(self,
               userId=None,
               skillSetId=None,
               collabSetId=None,
               goalSetId=None
    ):
        self.row = self.dbConnection.newRow()
        if userId:
            self.row._data.userId = userId

        if skillSetId:
            self.row._data.skillSetId = skillSetId

        if collabSetId:
            self.row._data.collabSetId = collabSetId

        if goalSetId:
            self.row._data.goalSetId = goalSetId

        self.row.commit()


class usersDao(object):
    def __init__(self, dbObj=None):
        if dbObj is None:
            dbObj = users

        self.dbConnection = dbConnection(dbObj)
        self.row = None
        # Let's garentee we'll only be getting one row. Think it makes sense
        # to only be dealing with one at a time.
        self.rowLimit = 1

    def delete(self):
        if self.row:
            self.row.delet()

    def load(self,
             userId=None,
             userName=None
    ):
        # self.results =
        self.row = self.dbConnection.loadRows(
            {
                'userId': userId,
                'userName': userName
            },
            self.rowLimit
        )

    def update(self,
               userName=None,
               userFullName=None
    ):
        if userName:
            self.row._data.userName = userName

        if userFullName:
            self.row._data.userFullName = userFullName

        self.row.commit()

    def create(self,
               userName=None,
               userFullName=None
    ):
        self.row = self.dbConnection.newRow()
        if userName:
            self.row._data.userName = userName

        if userFullName:
            self.row._data.userFullName = userFullName

        self.row.commit()


class skillsMappedToSkillSetDao(object):
    # same constructor as userSkillProgressPlanDao
    def __init__(self, dbObj=None):
        if dbObj is None:
            dbObj = skillsMappedToSkillSet

        self.dbConnection = dbConnection(dbObj)
        self.row = None
        # Let's garentee we'll only be getting one row. Think it makes sense
        # to only be dealing with one at a time.
        self.rowLimit = 1

    def delete(self):
        if self.row:
            self.row.delet()

    def load(self,
             skillId=None,
             skillSetId=None
             ):
        # self.results =
        self.row = self.dbConnection.loadRows(
            {
                'skillId': skillId,
                'skillSetId': skillSetId
            },
            self.rowLimit
        )

    def update(self,
               skillId=None,
               skillSetId=None
               ):
        if skillId:
            self.row._data.skillId = skillId

        if skillSetId:
            self.row._data.skillSetId = skillSetId

        self.row.commit()

    def create(self,
               skillId=None,
               skillSetId=None
               ):
        self.row = self.dbConnection.newRow()
        if skillId:
            self.row._data.skillId = skillId

        if skillSetId:
            self.row._data.skillSetId = skillSetId

        self.row.commit()


class collaboratorMappedToCollabSetDao(object):
    # same constructor as userSkillProgressPlanDao
    def __init__(self, dbObj=None):
        if dbObj is None:
            dbObj = collaboratorMappedToCollabSet

        self.dbConnection = dbConnection(dbObj)
        self.row = None
        # Let's garentee we'll only be getting one row. Think it makes sense
        # to only be dealing with one at a time.
        self.rowLimit = 1

    def delete(self):
        if self.row:
            self.row.delet()

    def load(self,
             collaboratorId=None,
             collabSetId=None
             ):
        # self.results =
        self.row = self.dbConnection.loadRows(
            {
                'collaboratorId': collaboratorId,
                'collabSetId': collabSetId
            },
            self.rowLimit
        )

    def update(self,
               collaboratorId=None,
               collabSetId=None
               ):
        if collaboratorId:
            self.row._data.collaboratorId = collaboratorId

        if collabSetId:
            self.row._data.collabSetId = collabSetId

        self.row.commit()

    def create(self,
               collaboratorId=None,
               collabSetId=None
               ):
        self.row = self.dbConnection.newRow()
        if collaboratorId:
            self.row._data.collaboratorId = collaboratorId

        if collabSetId:
            self.row._data.collabSetId = collabSetId

        self.row.commit()


class goalsMappedToGoalSetsDao(object):
    # same constructor as userSkillProgressPlanDao
    def __init__(self, dbObj=None):
        if dbObj is None:
            dbObj = goalsMappedToGoalSets

        self.dbConnection = dbConnection(dbObj)
        self.row = None
        # Let's garentee we'll only be getting one row. Think it makes sense
        # to only be dealing with one at a time.
        self.rowLimit = 1

    def delete(self):
        if self.row:
            self.row.delet()

    def load(self,
             goalId=None,
             goalSetId=None
             ):
        # self.results =
        self.row = self.dbConnection.loadRows(
            {
                'goalId': goalId,
                'goalSetId': goalSetId
            },
            self.rowLimit
        )

    def update(self,
               goalId=None,
               goalSetId=None
               ):
        if goalId:
            self.row._data.goalId = goalId

        if goalSetId:
            self.row._data.goalSetId = goalSetId

        self.row.commit()

    def create(self,
               goalId=None,
               goalSetId=None
               ):
        self.row = self.dbConnection.newRow()
        if goalId:
            self.row._data.goalId = goalId

        if goalSetId:
            self.row._data.goalSetId = goalSetId

        self.row.commit()


class goalsDao(object):
    # same constructor as userSkillProgressPlanDao
    def __init__(self, dbObj=None):
        if dbObj is None:
            dbObj = goals

        self.dbConnection = dbConnection(dbObj)
        self.row = None
        # Let's garentee we'll only be getting one row. Think it makes sense
        # to only be dealing with one at a time.
        self.rowLimit = 1

    def delete(self):
        if self.row:
            self.row.delet()

    def load(self,
             goalId=None,
             skillId=None
             ):
        # self.results =
        self.row = self.dbConnection.loadRows(
            {
                'goalId': goalId,
                'skillId': skillId
            },
            self.rowLimit
        )

    def update(self,
               goalId=None,
               skillId=None,
               skillLevel=None
               ):
        if goalId:
            self.row._data.goalId = goalId

        if skillId:
            self.row._data.skillId = skillId

        if skillLevel:
            self.row._data.skillLevel = skillLevel

        self.row.commit()

    def create(self,
               goalId=None,
               skillId=None,
               skillLevel=None
               ):
        self.row = self.dbConnection.newRow()
        if goalId:
            self.row._data.goalId = goalId

        if skillId:
            self.row._data.skillId = skillId

        if skillLevel:
            self.row._data.skillLevel = skillLevel

        self.row.commit()


class weeklySkillSetFeedBackDao(object):
    # same constructor as userSkillProgressPlanDao
    def __init__(self, dbObj=None):
        if dbObj is None:
            dbObj = weeklySkillSetFeedBack

        self.dbConnection = dbConnection(dbObj)
        self.row = None
        # Let's garentee we'll only be getting one row. Think it makes sense
        # to only be dealing with one at a time.
        self.rowLimit = 1

    def delete(self):
        if self.row:
            self.row.delet()

    def load(self,
             userId=None,
             weekId=None,
             skillSetId=None,
             skillId=None,
             collaboratorId=None
             ):
        # self.results =
        self.row = self.dbConnection.loadRows(
            {
                 'userId': userId,
                 'weekId': weekId,
                 'skillSetId': skillSetId,
                 'skillId': skillId,
                 'collaboratorId': collaboratorId
            },
            self.rowLimit
        )

    def update(self,
               userId=None,
               weekId=None,
               skillSetId=None,
               skillId=None,
               collaboratorId=None
               ):
        if userId:
            self.row._data.userId = userId

        if weekId:
            self.row._data.weekId = weekId

        if skillSetId:
            self.row._data.skillSetId = skillSetId

        if skillId:
            self.row._data.skillId = skillId

        if collaboratorId:
            self.row._data.collaboratorId = collaboratorId

        self.row.commit()

    def create(self,
               userId=None,
               weekId=None,
               skillSetId=None,
               skillId=None,
               collaboratorId=None
               ):
        self.row = self.dbConnection.newRow()
        if userId:
            self.row._data.userId = userId

        if weekId:
            self.row._data.weekId = weekId

        if skillSetId:
            self.row._data.skillSetId = skillSetId

        if skillId:
            self.row._data.skillId = skillId

        if collaboratorId:
            self.row._data.collaboratorId = collaboratorId

        self.row.commit()