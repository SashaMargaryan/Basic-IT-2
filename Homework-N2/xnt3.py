import math
x=float(input('nermuchel:x'))
y=float(input('nermuchel:y'))

print((math.sin(x)/math.cos(y))*math.fabs(math.pow(x,2)-y)/(math.pow(x,2)+math.pow(y,2))+math.log(math.pow(x,2)+1))