# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 18:50:42 2021

@author: MorenoW
"""

milam = float("{:.3f}".format(1609.344)) #mts
galam = float("{:.9f}".format(3.785411784)) #lts
def l100kmtompg(litres):
    mpg = (1 / (litres / 100)) * 1000 / milam *galam
    mpg = float("{:.15f}".format(mpg))
    return mpg

def mpgtol100km(miles):
    l100km = 1 / (((miles * milam) / galam) / 1000) * 100
    l100km = float("{:.15f}".format(l100km))
    return l100km

print("Conversión de l / 100km a mpg resulta:")
print("Para 3.9")
print(l100kmtompg(3.9),"mpg")
print("Para 7.5")
print(l100kmtompg(7.5),"mpg")
print("Para 10")
print(l100kmtompg(10.),"mpg")
print("")
print("Conversión de mpg a l / 100km resulta:")
print("Para 60.3")
print(mpgtol100km(60.3))
print("Para 31.4")
print(mpgtol100km(31.4))
print("Para 23.5")
print(mpgtol100km(23.5))
