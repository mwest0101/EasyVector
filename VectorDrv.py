
class Vector:
	@staticmethod
	def Int(val1=None,val2=None,val3=None,val4=None,val5=None):
		vec=0
		if val1 is not None:

			if val2 is None:
				vec=[0]*val1
			elif val3 is None:
				vec=[[0 for _ in range(val1)] for _ in range(val2)]
			elif val4 is None:
				vec=[[[0 for _ in range(val1)] for _ in range(val2)] for _ in range(val3)]
			elif val5 is None:
				vec=[[[[0 for _ in range(val1)] for _ in range(val2)] for _ in range(val3)] for _ in range(val4)]
			else:
				vec=[[[[[0 for _ in range(val1)] for _ in range(val2)] for _ in range(val3)] for _ in range(val4)] for _ in range(val5)]

		return vec

vec=Vector.Int(3,2,2,2,2)

vec[1][0]=10
print(vec)
