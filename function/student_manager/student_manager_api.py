from datetime import datetime

from flask import request
from flask_restful import Resource
from sqlalchemy import or_

from model.model import ConnectToDB, Student
from libraries.general import standardizedData

Session = ConnectToDB()

class StudentAPI(Resource):

	def get(self):
		try:
			session = Session()
			parameters = request.args
			query = session.query(Student)
			if "search" in parameters and parameters['search'] != "":
				search_values = parameters['search'].split(",")
				for search_value in search_values:
					query = query.filter(or_(key.like('%'+ search_value +'%')\
						for key in Student.__table__.columns))
			records = query.all()
			for i in range(len(records)):
				records[i] = standardizedData(records[i])
			return records
		except Exception as exp:
			print (exp)
			return False