from EasyVector import *
	# 	print(self)
vec=Vector.Int(3,2,2)
vec[1][0][0]=5
print(vec)

vec=Vector.Char(2,2,2)
vec[1][0][0]='c'
print(vec)

vec=Vector.Float(2,2,2)
vec[1][0][0]=0.0
print(vec)

vec=Vector.String(2,2,2)
vec[0][0][0]="Hola"
vec[1][1][0]="Mundo"
print(vec)