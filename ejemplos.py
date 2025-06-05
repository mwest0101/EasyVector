
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

vec=Vector.Float(5,5)
vec[1][0]=0.0
print(vec)
Vector.print(vec)
print("")

vec=Vector.String(4,4)
vec[0][0]="Ho"
vec[0][1]="la"
vec[1][1]="Mundo"
print(vec)
Vector.print(vec)
print("")
vec=Vector.Float(2,2,3)
vec[0][0][0]=1.0
vec[0][0][1]=1.1
vec[0][0][2]=1.2
vec[0][1][0]=2.0
vec[0][1][1]=2.1
vec[0][1][2]=2.2
vec[1][0][0]=2.0
vec[1][0][1]=2.1
vec[1][0][2]=2.2
vec[1][1][0]=2.0
vec[1][1][1]=2.1
vec[1][1][2]=2.2

print(vec)
Vector.print(vec)
vec=Vector.Float(2,2,2,3)
vec[0][0][0][0]=1.0
vec[0][0][0][1]=1.1
vec[0][0][0][2]=1.2


vec[0][0][1][0]=2.0
vec[0][0][1][1]=2.1
vec[0][0][1][2]=2.2

vec[0][1][0][0]=2.0
vec[0][1][0][1]=2.1
vec[0][1][0][2]=2.2

vec[0][1][1][0]=2.0
vec[0][1][1][1]=2.1
vec[0][1][1][2]=2.2
print(vec)
Vector.print(vec)
print("")

vec=Vector.Int(2,3,3)
vec[1][2][2]=1
print(vec)
Vector.print(vec)
print("")



# vec=Vector.Int(2,3,3,3)

# print(vec)
# Vector.print(vec)
# print("")