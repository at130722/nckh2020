from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import *
from sqlalchemy.orm import *
from sqlalchemy import *

Base = declarative_base()


# khoi tao ket noi vao co so du lieu
def ConnectToDB():
	engine = create_engine('mysql+mysqldb://nckh:123456Aa!@127.0.0.1/nckh?charset=utf8')
	Session = sessionmaker(bind=engine)
	return Session


class Student(Base):
	__tablename__ = 'student'

	id = Column(String, primary_key=True)
	name = Column(String)

class Attendance(Base):
	__tablename__ = 'attendance'


	id = Column(Integer, primary_key=True)
	student_id = Column(String)
	time = Column(String)
	path = Column(String)