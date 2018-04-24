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
    userFullName = Column(String)
    userName = Column(String)
    __table_args__ = (UniqueConstraint('userName', name='_username_uc'),
                      )


class skillsMappedToSkillSet(Base):
    __tablename__ = 'skillsMappedToSkillSet'
    # Here we'll define which skills are in a skill set.

    skillSetId = Column(Integer, primary_key=True)
    skillId = Column(Integer, primary_key=True, nullable=False, default=None)


class collaboratorMappedToCollabSet(Base):
    __tablename__ = 'collaboratorMappedToCollabSet'
    # Here we'll define which collaborators are in a collab set.

    collabSetId = Column(Integer, primary_key=True)
    collaboratorId = Column(Integer, primary_key=True, nullable=False, default=None)


class goalsMappedToGoalSets(Base):
    __tablename__ = 'goalsMappedToGoalSets'
    # Here we'll define what goals are in the goal set.

    goalSetId = Column(Integer, primary_key=True)
    goalId = Column(Integer, primary_key=True, nullable=False, default=None)


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