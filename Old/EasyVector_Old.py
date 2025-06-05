
class Vector:
	@staticmethod
	def Int(val1=None,val2=None,val3=None,val4=None,val5=None,val6=None,val7=None,val8=None,val9=None,val10=None):
		return Vector.createVec(0,val1,val2,val3,val4,val5,val6,val7,val8,val9,val10)

	@staticmethod
	def Char(val1=None,val2=None,val3=None,val4=None,val5=None,val6=None,val7=None,val8=None,val9=None,val10=None):
		return Vector.createVec(' ',val1,val2,val3,val4,val5,val6,val7,val8,val9,val10)
  
	@staticmethod
	def Float(val1=None,val2=None,val3=None,val4=None,val5=None,val6=None,val7=None,val8=None,val9=None,val10=None):
		return Vector.createVec(0.0,val1,val2,val3,val4,val5,val6,val7,val8,val9,val10)
	@staticmethod
	def String(val1=None,val2=None,val3=None,val4=None,val5=None,val6=None,val7=None,val8=None,val9=None,val10=None):
		return Vector.createVec(" ",val1,val2,val3,val4,val5,val6,val7,val8,val9,val10)
	
	@staticmethod
	def createVec(varType=0,val1=None,val2=None,val3=None,val4=None,val5=None,val6=None,val7=None,val8=None,val9=None,val10=None):
		vec=0
		if val1 is not None:
			if val2 is None:
				vec = [varType] * val1
			elif val3 is None:
				vec = [[varType for _ in range(val1)] for _ in range(val2)]
			elif val4 is None:
				vec = [[[varType for _ in range(val1)] for _ in range(val2)] for _ in range(val3)]
			elif val5 is None:
				vec = [[[[varType for _ in range(val1)] for _ in range(val2)] for _ in range(val3)] for _ in range(val4)]
			elif val6 is None:
				vec = [[[[[varType for _ in range(val1)] for _ in range(val2)] for _ in range(val3)] for _ in range(val4)] for _ in range(val5)]
			elif val7 is None:
				vec = [[[[[[varType for _ in range(val1)] for _ in range(val2)] for _ in range(val3)] for _ in range(val4)] for _ in range(val5)] for _ in range(val6)]
			elif val8 is None:
				vec = [[[[[[[varType for _ in range(val1)] for _ in range(val2)] for _ in range(val3)] for _ in range(val4)] for _ in range(val5)] for _ in range(val6)] for _ in range(val7)]
			elif val9 is None:
				vec = [[[[[[[[varType for _ in range(val1)] for _ in range(val2)] for _ in range(val3)] for _ in range(val4)] for _ in range(val5)] for _ in range(val6)] for _ in range(val7)] for _ in range(val8)]
			elif val10 is None:
				vec = [[[[[[[[[varType for _ in range(val1)] for _ in range(val2)] for _ in range(val3)] for _ in range(val4)] for _ in range(val5)] for _ in range(val6)] for _ in range(val7)] for _ in range(val8)] for _ in range(val9)]
			else:
				vec = [[[[[[[[[[varType for _ in range(val1)] for _ in range(val2)] for _ in range(val3)] for _ in range(val4)] for _ in range(val5)] for _ in range(val6)] for _ in range(val7)] for _ in range(val8)] for _ in range(val9)] for _ in range(val10)]
		return vec