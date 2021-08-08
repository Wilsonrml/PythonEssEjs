# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 20:27:50 2021

@author: MorenoW
"""

def isYearLeap(year):
    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        return  True
    else:
        return False
    
def daysInMonth(year,month):
    if year < 1900 or month < 1 or month > 12:
        return None
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2 and isYearLeap(year):
        return 29
    else:
        return 28

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]

for i in range(len(testYears)):
    year = testYears[i]
    month = testMonths[i]
    print(year, month, "->", end=" ")
    result = daysInMonth(year, month)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")

"""year = int(input("Ingrese un año: "))
month = int(input("Ingrese un mes: "))
days = daysInMonth(year, month)
if days == None:
    print("\n"+str(days)+" -> Año o Mes incorrectos!")
else:
    print("\nEl número de días es: ", days)
"""
