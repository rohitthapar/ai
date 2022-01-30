D = {1:"One", 2:"Two", 3:"Three", 4: "Four", 5:"Five"}
D[6] = "Six"
print(D)
del D[2]
print(D)
print(D.has_key(6))
count = 0
count = int(count)
print(sum([len(D[x]) for x in D if isinstance(D[x], list)]))
# print(count)