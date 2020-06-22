def standardizedData(obj, del_param=None, param=None):
		data = {}
		try:
			obj = obj.__dict__
		except:
			return None
		try:
			if '_sa_instance_state' in obj:
				del obj["_sa_instance_state"]
		except:
			pass
		if del_param != None:
			for d in del_param:
				try:
					del obj[d]
				except:
					pass
		if param != None:
			for p in param:
				data[p] = obj[param[p]]
			return data

		return obj