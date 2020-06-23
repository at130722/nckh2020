from datetime import datetime

from flask import request
from flask_restful import Resource
from sqlalchemy import or_

from model.model import ConnectToDB, Student, AttendanceCount
from libraries.general import standardizedData

Session = ConnectToDB()

class AttendanceCountAPI(Resource):

	def get(self):
		try:
			session = Session()
			parameters = request.args
			query = session.query(AttendanceCount)
			if "search" in parameters and parameters['search'] != "":
				search_values = parameters['search'].split(",")
				for search_value in search_values:
					query = query.filter(or_(key.like('%'+ search_value +'%')\
						for key in AttendanceCount.__table__.columns))
			records = query.all()
			for i in range(len(records)):
				records[i] = standardizedData(records[i])
				records[i]['time'] = str(records[i]['time'])
			print (records)
			return records
		except Exception as exp:
			print (exp)
			return False