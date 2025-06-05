
from EasyVectorK import *
	# 	print(self)
vec=Vector.Int(10)
vec[1]=5
print(vec)

vec=Vector.Char(5,2)
vec[1][0]='c'
print(vec)

vec=Vector.Float(3,3,3)
vec[1][0][0]=0.0
print(vec)

vec=Vector.String(4,4)
vec[0][0]="Hola"
vec[1][1]="Mundo"
print(vec)