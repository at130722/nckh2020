import csv
from datetime import datetime

from flask import request, send_file
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
				name = records[i].student.name
				records[i] = standardizedData(records[i], ['student'])
				records[i]['name'] = name
				records[i]['time'] = str(records[i]['time'])
			attendance_count = []
			student_list = {}
			for record in records:
				attendance_count.append(record['time'].split(" ")[0])
				if record['student_id'] not in student_list:
					student_list[record['student_id']] = []
					student_list[record['student_id']].append(record)
				else:
					student_list[record['student_id']].append(record)
			data = {
				'data': student_list,
				'att_count': sorted(list(set(attendance_count)))
			}
			return data
		except Exception as exp:
			raise (exp)
			return False 

	# Diem danh trong cung 1 ngay - xoa ban ghi cu ghi de du lieu moi !!!!!!!!!
	def post(self):
		try:
			session = Session()
			student_list = []
			students = session.query(Student).all()
			for i in range(len(students)):
				students[i] = standardizedData(students[i])
				student_list.append(students[i]['id'])
			print (student_list)
			current_time = datetime.now()
			request_data = request.json['data']
			print (request_data)
			for data in request_data:
				at_info = Attendance(
					student_id = data['mssv'],
					time = current_time,
					path = data['path'],
					status = 1
				)
				session.add(at_info)
				print ("remove", data['mssv'])
				student_list.remove(data['mssv'])
			print ("student_list", student_list)
			for student in student_list:
				at_info = Attendance(
					student_id = student,
					time = current_time,
					path = None,
					status = 0
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

class DownloadListAPI(Resource):

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
				name = records[i].student.name
				records[i] = standardizedData(records[i], ['student'])
				records[i]['name'] = name
				records[i]['time'] = str(records[i]['time'])
			attendance_count = []
			student_list = {}
			for record in records:
				attendance_count.append(record['time'].split(" ")[0])
				if record['student_id'] not in student_list:
					student_list[record['student_id']] = []
					student_list[record['student_id']].append(record)
				else:
					student_list[record['student_id']].append(record)
			data = {
				'data': student_list,
				'att_count': sorted(list(set(attendance_count)))
			}
			with open('static/csv/attendance_list.csv', mode='w') as csv_file:
				fieldnames = ['Pos', 'Name', 'Student ID']
				for att_count in data['att_count']:
					fieldnames.append(att_count)
				writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
				writer.writeheader()
				i = 1
				for student_id in data['data']:
					print ("Std", student_id)
					content = {
						'Pos': i,
						'Name': data['data'][student_id][0]['name'],
						'Student ID': student_id
					}
					i += 1
					for att_info in data['data'][student_id]:
						if att_info['status'] == 1:
							content[att_info['time'].split(" ")[0]] = att_info['time'].split(" ")[1]
							print (content)
						else:
							content[att_info['time'].split(" ")[0]] = "Nghi hoc"
					writer.writerow(content)
			return send_file(
				"static/csv/attendance_list.csv",
				mimetype='text/csv',
                attachment_filename='attendance_list.csv',
                as_attachment=True
			)
		except Exception as exp:
			raise (exp)
			return False
		finally:
			session.close()
		