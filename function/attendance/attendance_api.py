from datetime import datetime

from flask import request
from flask_restful import Resource
from sqlalchemy import or_

from model.model import ConnectToDB, Student, Attendance
from libraries.general import standardizedData

Session = ConnectToDB()

class AttendanceAPI(Resource):

	def get(self):
		try:
			session = Session()
			parameters = request.args
			query = session.query(Attendance)
			if "search" in parameters and parameters['search'] != "":
				search_values = parameters['search'].split(",")
				for search_value in search_values:
					query = query.filter(or_(key.like('%'+ search_value +'%')\
						for key in Attendance.__table__.columns))
			records = query.all()
			for i in range(len(records)):
				records[i] = standardizedData(records[i])
				records[i]['time'] = str(records[i]['time'])
			print (records)
			return records
		except Exception as exp:
			print (exp)
			return False

	def post(self):
		try:
			session = Session()
			current_time = datetime.now()
			request_data = request.json['data']
			print (request_data)
			for data in request_data:
				at_info = Attendance(
					student_id = data['mssv'],
					time = current_time,
					path = data['path']
				)
				session.add(at_info)
			try:
				session.commit()
			except Exception as exp:
				print (exp)
				session.rollback()
				return False
			return True
		except Exception as exp:
			print (exp)
			return False

class AttendanceOneAPI(Resource):

	def get(self, dd_id):
		try:
			session = Session()
			record = session.query(Attendance).filter_by(id = dd_id).one()
			record = standardizedData(record)			
			return status_code_200("", record)
		except Exception as exp:
			print (exp)
			return status_code_500("")
		finally:
			session.close()
		