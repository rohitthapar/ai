#gross salary of an employee
# Write a Python Program to input basic salary of an employee and calculate its Gross
# salary according to following: Basic Salary <= 10000 : HRA = 20%, DA = 80% Basic
# Salary <= 20000 : HRA = 25%, DA = 90% Basic Salary > 20000 : HRA = 30%, DA =
# 95%

sal = int(input("Enter basic salary "))
if sal<=10000:
    sal = float(sal + 0.2*sal + 0.8*sal)
elif sal<=20000:
    sal = float(sal + 0.25*sal + 0.9*sal)
elif sal>20000:
    sal = float(sal + 0.3*sal + 0.95*sal)
print(sal)
