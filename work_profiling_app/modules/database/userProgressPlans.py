from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import UniqueConstraint

Base = declarative_base()

class userSkillProgressPlan(Base):
    __tablename__ = 'userSkillProgressPlan'
    # here we'll define what skill sets a particular person wants to work on,
    # who they want to work on them with, and what their goal is.

    userId = Column(Integer, primary_key=True, default=None)
    skillSetId = Column(Integer, primary_key=True, default=None)
    collabSetId = Column(Integer, primary_key=True, default=None)
    goalSetId = Column(Integer, primary_key=True, default=None)
    goalDeadlineInWeeks = Column(Integer, primary_key=True, default=None)


class users(Base):
    __tablename__ = 'users'

    userId = Column(Integer, primary_key=True)
    userFullName = Column(String, nullable=False)
    userName = Column(String, nullable=False, unique=True)


class skills(Base):
    __tablename__ = 'skills'

    skillId = Column(Integer, primary_key=True)
    skillName = Column(String, nullable=False, unique=True)
    skillDescription = Column(String, nullable=False)


class skillsMappedToSkillSet(Base):
    __tablename__ = 'skillsMappedToSkillSet'
    # Here we'll define which skills are in a skill set.

    skillSetId = Column(Integer, primary_key=True)
    skillId = Column(Integer, primary_key=True, nullable=False, default=None)
    ## This should be linked to what you want to work on. i.e. work life, a project, etc.
    skillSetName = Column(String, nullable=False, unique=True)


class collaboratorMappedToCollabSet(Base):
    __tablename__ = 'collaboratorMappedToCollabSet'
    # Here we'll define which collaborators are in a collab set.

    collabSetId = Column(Integer, primary_key=True)
    collaboratorId = Column(Integer, primary_key=True, nullable=False, default=None)
    collabAssocSkillSetId = Column(Integer, primary_key=True)
    collabSetName = Column(String, nullable=False) ## this will need a foreign key dependency on skillSetName


class goalsMappedToGoalSets(Base):
    __tablename__ = 'goalsMappedToGoalSets'
    # Here we'll define what goals are in the goal set.

    goalSetId = Column(Integer, primary_key=True)
    goalId = Column(Integer, primary_key=True, nullable=False, default=None)
    goalSetName = Column(String, nullable=False) ## this will need a foreign key dependency on skillSetName


class goals(Base):
    __tablename__ = 'goals'

    goalId = Column(Integer, primary_key=True)
    skillId = Column(Integer, primary_key=True, nullable=False, default=None)
    skillLevel = Column(Integer, nullable=False, default=None)


class weeklySkillSetFeedBack(Base):
    __tablename__ = 'weeklySkillSetFeedBack'
    # here we'll define what skill sets a particular person wants to work on,
    # who they want to work on them with, and what their goal is.

    userId = Column(Integer, primary_key=True, default=None)
    weekId = Column(Integer, primary_key=True)
    skillSetId = Column(Integer, primary_key=True, nullable=False, default=None)
    skillId = Column(Integer, primary_key=True, nullable=False, default=None)
    collaboratorId = Column(Integer, primary_key=True, nullable=False, default=None)
    skillLevel = Column(Integer, nullable=False, default=None)

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///userProgressPlans.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)