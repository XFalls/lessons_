import math
a= float(input ('number a:'))
b= float(input ('number b:'))
c= float(input ('number c:'))
x1 = (( -b + math.sqrt(b ** 2 - 4 * a * c)) / 2)
x2 = (( -b - math.sqrt(b ** 2 - 4 * a * c)) / 2)
print('first x'), print(round(x1, 2))
print('second x'), print(round(x2, 2))
input('Press Enter to exit\n')