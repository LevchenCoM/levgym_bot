from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship

from db import Base


class TrainingProgram(Base):
    __tablename__ = 'training_programs'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    created = Column(DateTime)
    user_id = Column(Integer)


class Training(Base):
    __tablename__ = 'trainings'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    training_program = relationship('TrainingProgram', backref='training')


class ExerciseType(Base):
    __tablename__ 'exercise_types'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    training = relationship('TrainingProgram', backref='exercise_type')


class Exercise(Base):
    __tablename__ = 'exercises'

    id = Column(Integer, primary_key=True)
    exercise_id = Column(Integer)
    start_date = Column(DateTime)
    end_date = Column(DateTime)

    def __init__(self, exercise_id, start_date, end_date=None):
        self.exercise_id = exercise_id
        self.start_date = start_date
        self.end_date = end_date
