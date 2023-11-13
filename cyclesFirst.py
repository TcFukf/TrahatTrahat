import math
#n = int (input("n:"))
#x = int (input("x:"))
n = 18
x = 2
print(f"n:{n}, x:{x}")
Y = math.pi/2
K = 1
sign = -1
for i in range(n-1):
    Y= Y + sign* 1/( (x**2) * K )
    K+=2
    sign*=-1
print(Y)
