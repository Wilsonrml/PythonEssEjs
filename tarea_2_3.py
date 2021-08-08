# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 20:49:25 2021

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

def dayOfYear(year,month,day):
    totalDays = day
    if year < 1900 or month < 1 or month > 12 or day < 1 or day > 31:
        return None
    for i in range(1,month,1):
        totalDays += daysInMonth(year,i)        
    return totalDays

year = int(input("Ingrese un año: "))
month = int(input("Ingrese un mes: "))
day = int(input("Ingrese un día: "))
noDias = dayOfYear(year, month, day);
print("\nLos días correspondientes al año y fecha ingresados son: ", noDias)
