'''
Created on Jan 4, 2019
This program performs temperature conversions between the three major 
temperature scales: fahrenheit, celsius and kelvin. Enter a temperature 
in one scale and the program converts that temperature to the other
two scales.
@author: ebrie
'''
scale = input("Enter scale (c/f/k): ")
if scale == 'c':
    celsius = float(input('Enter Celsius temp: '))
    fahrenheit = (9/5) * celsius + 32
    kelvin = celsius + 273.15
elif scale == 'f':
    fahrenheit = float(input('Enter Fahrenheit temp: '))
    celsius = (5/9) * (fahrenheit - 32)
    kelvin = celsius + 273.15
else:
    kelvin = float(input('Enter Kelvin temp: '))
    celsius = kelvin - 273.15
    fahrenheit = (9/5) * celsius + 32

if scale != 'c':
    print('Celsius = ' + str(round(celsius, 3)))
if scale != 'f':
    print('Fahrenheit = ' + str(round(fahrenheit, 3)))
if scale != 'k':
    print('Kelvin = ' + str(round(kelvin, 3)))