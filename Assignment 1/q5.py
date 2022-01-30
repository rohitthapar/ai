#print leap years between two years
n = int(input("Enter first year "))
m = int(input("Enter second year "))
for i in range(n,m+1,1):
    if i%4 == 0 and i%100 != 0:
        print(i,"is a leap year")
    elif i%400 == 0:
        print(i, "is a leap year")
    else:
        print(i, "is not a leap year")
