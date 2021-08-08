# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 19:53:01 2021

@author: MorenoW
"""

def fibonacci(number):
    a = 0
    b = 1
    while a < number:
        print(a, end=" ")
        c = a + b
        a = b
        b = c
        #a, b = b, a+b        
    #print()

n = int(input("Ingrese un número para calcular: "))
print("El Fibonacci de",n,"es: ")
fibonacci(n)
