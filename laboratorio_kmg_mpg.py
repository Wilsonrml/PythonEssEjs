# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 20:23:51 2021

@author: MorenoW
"""
milam = float(1609.344) #mts
galam = float(3.785411784) #lts

def l100kmtompg(liters):
    mpg = (1 / (liters/100)) * galam * 1000 / milam
    mpg = float(mpg)
    return mpg

def mpgtol100km(miles):
    l100km = 1 / (((miles * milam) / galam) / 1000) * 100
    l100km = float(l100km)
    return l100km

print("Conversión de Consumo de Combustible")
print("{:.14f}".format(l100kmtompg(3.9)))
print("{:.14f}".format(l100kmtompg(7.5)))
print("{:.14f}".format(l100kmtompg(10.)))

print("{:.15f}".format(mpgtol100km(60.3)))
print("{:.15f}".format(mpgtol100km(31.4)))
print("{:.15f}".format(mpgtol100km(23.5)))