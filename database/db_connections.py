from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class profilesDB(Base):
    __tablename__ = 'userProfiles'

    user_id = Column(Integer, primary_key=True, default=None)
    skill_id = Column(Integer, primary_key=True, default=None)
    collab_id = Column(Integer, primary_key=True, default=None)
    week_id = Column(Integer, primary_key=True, default=None)
    feedback = Column(Integer, primary_key=False, nullable=True, default=None)


class userNamesDB(Base):
    __tablename__ = 'userNames'

    user_id = Column(Integer, primary_key=True, default=None)
    user_name = Column(String(1000), primary_key=False, nullable=False, default=None)


class skillDescriptionsDB(Base):
    __tablename__ = 'skillDescriptions'

    skill_id = Column(Integer, primary_key=True, default=None)
    skill_description = Column(String(1000), primary_key=False, nullable=False, default=None)


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///profiles.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)