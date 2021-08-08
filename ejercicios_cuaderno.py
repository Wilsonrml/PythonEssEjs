# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 18:20:23 2021

@author: MorenoW
"""

#15
class Ascensor:
    def __init__(self, floor_numbers, floor_types):
        self._floor_numbers = floor_numbers
        self._floor_types = floor_types
        self._number_to_type_dict = dict(zip(floor_numbers, floor_types)) 
        self._type_to_number_dict = dict(zip(floor_types, floor_numbers)) 
        
    def ask_which_floor(self, floor_type):    
        if floor_type in self._floor_types:
            print('The {} floor is the number: {}.'.format(floor_type, self._type_to_number_dict[floor_type]))
        else:
            print('There is no {} floor in this building.'.format(floor_type))
    
    def go_to_floor(self, floor_number):
        if floor_number in self._floor_numbers:
            print('Go to the number {} of the {} floor.'.format(floor_number, self._number_to_type_dict[floor_number]))
        else:
            print('In this building there is no number {} floor.'.format(floor_number))

#floor_types = ['Estacionamiento', 'Negocios', 'Área de restaurantes', 'Oficinas'] 
floor_types = ['Parking', 'Shops', 'Food Court', 'Offices']
floor_numbers = range(-1,4)

a = Ascensor(floor_numbers, floor_types)

a.go_to_floor(1)
a.go_to_floor(-2)
a.ask_which_floor('Offices')
a.ask_which_floor('Swimming Pool')


"""

#14
floor_types = ['Parking', 'Shops', 'Food Court', 'Offices']
floors_numbers = range(-1,3)

list1 = zip(floors_numbers,floor_types)
elevator_dict = dict(list1)
print(elevator_dict[-1])

#13
floor_types = ['Parking', 'Shops', 'Food Court', 'Offices']
floor_numbers = range(-1,3)

list1 = zip(floor_types,floor_numbers)
zipped = list(list1) 
print(zipped)

#12
def smart_thermostat(temp, people_in):
    if temp < 20 and people_in:
        command = "calefacción encendida"
    elif temp >= 23 or people_in == False:
        command = "calefacción apagada"
    else:
        command = "No hacer nada"
    return command

print(smart_thermostat(21,True))

#11
seq = ['data','salt' ,'dairy','cat', 'dog']
print(list(map(lambda st: (st.upper()), seq)))

#10
seq = ['data','salt' ,'dairy','cat', 'dog']
print(list(filter(lambda st: (st[0] != 'd'), seq)))

#9
def countIoT(st):
    count = 0
    for item in st.split():
        if item == 'IoT':
            count+=1
    return count
print(countIoT('I don\'t know how to spell IoT ! Is it IoT or iot ? What does iot mean anyway?'))

#8
def findInternet(cadena):
    return 'internet' in cadena.lower().split()
print(findInternet('The Internet Engineering Task Force was created in 1986'))

#7
def GetDomain(correo):
    return correo.split('@')[-1]

print(GetDomain('user@domain.com'))

#6
La principal diferencia es que en la tupla el conjunto de datos no pueden ser modificados; es decir los valores son inmutables, y a diferencia de la lista se declara entre paréntesis.

#5
d = {'k1':['val1','val2','val3',{'we':['need','to','go',{'deeper':[1,2,3,'that']}]}]}
d['k1'][3]['we'][3]['deeper'][3]


#4
lst = ['a','b',[4,10,11],['c',[1,66,['this']],2,111],'e',7]
print(lst[3][1][2][0])

#3
mountain = "Mt. Everest"
height = 8848
print("La altura del {} es de {} metros.".format( mountain , height ))

#2
s = "¡Este curso es increíble!"
s.split()
print(s.split())

#1
3**5
"""