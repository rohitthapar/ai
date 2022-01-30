from __future__ import print_function
import numpy as np
def Rand(start, end, num):
    res = []
    for j in range(num):
        res.append(np.random.randint(start, end))
    return res
num = 100
start = 100
end = 900
print("-----ODD NUMBERS-----")
for num in Rand(start, end, num):
    if num % 2 != 0:
        print(num , end = ' ')
print(" ")
print("-----EVEN NUMBERS-----")
for num in Rand(start, end, num):
    if num % 2 == 0:
        print(num , end = ' ')
print(" ")
prime = []
print("-----PRIME NUMBERS-----")
for num in Rand(start, end, num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                break
            else:
                prime.append(num)
print(np.unique(prime))
# print(Rand(start, end, num))