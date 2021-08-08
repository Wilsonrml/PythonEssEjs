# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 22:05:05 2021

@author: MorenoW
"""

def isPrime(number):
    for i in range(2,number,1):
        if number%i == 0:
            return False
    return True
#n = int(input("Ingrese un número a verificar: "))
#isPrime(n)
print("Números Primos en el rango del 1 al 20:")
for i in range (1,20):
    if isPrime(i+1):
        print(i+1, end=" ")
