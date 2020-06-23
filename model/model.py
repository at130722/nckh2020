from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import *
from sqlalchemy.orm import *
from sqlalchemy import *

Base = declarative_base()

def ConnectToDB():
	engine = create_engine('mysql+mysqldb://nckh:123456Aa!@127.0.0.1/nckh?charset=utf8')
	Session = sessionmaker(bind=engine)
	return Session


class Student(Base):
	__tablename__ = 'student'

	id = Column(String, primary_key=True)
	name = Column(String)

	attendance = relationship('Attendance', uselist=False, back_populates="student")


class Attendance(Base):
	__tablename__ = 'attendance'

	id = Column(Integer, primary_key=True)
	student_id = Column(String, ForeignKey('student.id'))
	time = Column(String)
	path = Column(String)
	status = Column(Integer)

	student = relationship("Student", back_populates="attendance")

class AttendanceCount(Base):
	__tablename__ = 'attendance_count'

	id = Column(Integer, primary_key=True)
	time = Column(String)