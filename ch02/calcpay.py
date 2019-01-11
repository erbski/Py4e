'''
Created on Jan 4, 2019
This program calculates the gross pay given the number of hours worked
and the pay rate.
@author: ebrie
'''
hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
pay = round(int(hours) * float(rate), 2)
print('Pay: $' + str(pay))