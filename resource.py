from flask import Flask
from flask_restful import Resource, Api

from function.diemdanh.diem_danh_api import DiemDanhAPI

app = Flask(__name__)
api = Api(app)


api.add_resource(DiemDanhAPI, '/api/diemdanh', methods = ['GET', 'POST'])


if __name__ == '__main__':
	try:
		app.run(host='0.0.0.0', port=3000, debug=True)
	except Exception as exp:
		print (exp)
