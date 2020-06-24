from flask import Flask, render_template
from flask_restful import Resource, Api

from function.attendance.attendance_api import AttendanceAPI, DownloadListAPI
from function.student_manager.student_manager_api import StudentAPI
from function.start_attendance.start_attendance_api import StartAttendanceAPI

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/attendance')
def attendance():
	return render_template('attendance.html')

@app.route('/attendance_info')
def attendance_info():
	return render_template('attendance_info.html')

api.add_resource(AttendanceAPI, '/api/attendance', methods = ['GET', 'POST'])
api.add_resource(DownloadListAPI, '/api/attendance/download', methods=['GET'])
api.add_resource(StartAttendanceAPI, '/api/start_attendance', methods=['POST'])
api.add_resource(StudentAPI, '/api/student', methods=['GET'])


if __name__ == '__main__':
	try:
		app.run(host='0.0.0.0', port=3000, debug=True)
	except Exception as exp:
		print (exp)
