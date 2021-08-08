# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 19:55:50 2021

@author: MorenoW
"""

def isYearLeap(year):
    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        return  True
    else:
        return False

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]

for i in range(len(testData)):
    year = testData[i]
    print(year,"->",end=" ")
    result = isYearLeap(year)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")
    
"""year = int(input("Ingrese un año: "))
if isYearLeap(year):
    print("El año es bisiesto")
else:
    print("El año es normal")
"""
