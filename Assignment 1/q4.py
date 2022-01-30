#common elements from two lists
def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
 
    if (a_set & b_set):
        print(a_set & b_set)
    else:
        print("No common elements")
lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele) 
lst1 = []
m = int(input("Enter number of elements : "))
for i in range(0, m):
    ele = int(input())
    lst1.append(ele) 
common_member(lst,lst1)
