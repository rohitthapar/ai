import numpy as np
def Rand(start, end, num):
    res = []
    for j in range(num):
        res.append(np.random.randint(start, end))
    return res
num = 10
start = 20
end = 40
print(Rand(start, end, num))