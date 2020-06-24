from io import BytesIO
import time
import base64
from datetime import datetime

from PIL import Image
from flask import request
from flask_restful import Resource
from sqlalchemy import or_

from model.model import ConnectToDB, Student, AttendanceCount
from libraries.general import standardizedData

Session = ConnectToDB()

class StartAttendanceAPI(Resource):

	def post(self):
		try:
			tname = str(int(time.time()))
			data = request.json['data']
			print (data)
			data = data.split(",")
			data = data[len(data) - 1]
			filename = f"static/attendance_img/img_{tname}.png"
			img = Image.open(BytesIO(base64.b64decode(data)))
			img.save(filename, 'PNG')
			time.sleep(3)
			return f"static/attendance_img/img_{tname}_attendanced.png"
		except Exception as exp:
			raise (exp)
			return False