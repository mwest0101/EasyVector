
from EasyVector import *
	# 	print(self)
vec=Vector.Int(10)
vec[1]=5
print(vec)
Vector.print(vec)
print("")

vec=Vector.Char(5,2)
vec[1][0]='c'
print(vec)
Vector.print(vec)
print("")

vec=Vector.Float(2,2)
vec[1][0]=0.0
print(vec)
Vector.print(vec)
print("")

vec=Vector.String(4,4)
vec[0][0]="Hola"
vec[1][1]="Mundo"
print(vec)
Vector.print(vec)
print("")


vec=Vector.Float(2,2)
# vec[1][0][0][0][0]=0.0
print(vec)
Vector.print(vec)
print("")