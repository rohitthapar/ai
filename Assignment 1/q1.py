import math
x = int(input("Enter value of x "))
n = int(input("Enter value of n "))
sm = 0
sm = float(sm)
for i in range(1,n+1,1):
    y = math.pow(x,i)
    z = math.factorial(i)
    sm = float(sm + y/z)
print(sm+1)