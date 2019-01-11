'''
Created on Jan 10, 2019
This program calculates the gross pay given the number of hours worked
and the pay rate. Any hours over 40 is handled as overtime using a pay
rate of 1.5 times the base pay rate.
@author: ebrie
'''
totHours = int(input('Enter Hours: '))
if totHours <= 40:
    basHours = totHours
    ovtHours = 0
else:
    basHours = 40
    ovtHours = totHours - 40

basRate = float(input('Enter Rate: '))
ovtRate = basRate * 1.5

# Calculate/print base pay
basPay = round((basHours * basRate), 2)
print('Base Pay:     $' + str(basPay))

# Calculate/print overtime pay
ovtPay = 0
if ovtHours > 0:
    ovtPay = round((ovtHours * ovtRate), 2)
    print('Overtime Pay: $' + str(ovtPay))

# Calculate/print total pay
totPay = basPay + ovtPay
print('Total Pay:    $' + str(totPay))