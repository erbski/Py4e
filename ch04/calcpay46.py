'''
Created on Jan 10, 2019
This program calculates the gross pay given the number of hours worked
and the pay rate. Any hours over 40 is handled as overtime using a pay
rate of 1.5 times the base pay rate. User is prompted for correct input 
if original input is bad.
@author: ebrie
'''
HOURS_FULLTIME = 40
RATE_MULTIPLIER = 1.5

def computepay(hours, rate):
    return round((hours * rate), 2)

hours = input('Enter Hours: ')
try:
    totHours = int(hours)
except:
    hours = input('Invalid input. Please reenter Hours: ')
    totHours = int(hours)
    
if totHours <= HOURS_FULLTIME:
    basHours = totHours
    ovtHours = 0
else:
    basHours = HOURS_FULLTIME
    ovtHours = totHours - HOURS_FULLTIME

rate = input('Enter Rate: ')
try:
    basRate = float(rate)
except:
    rate = input('Invalid input. Please reenter Rate: ')
    basRate = float(rate)
ovtRate = basRate * RATE_MULTIPLIER

# Calculate/print base pay
basPay = basHours * basRate
print('Base Pay:     $' + str(basPay))

# Calculate/print overtime pay
ovtPay = 0
if ovtHours > 0:
    ovtPay = computepay(ovtHours, ovtRate)
    print('Overtime Pay: $' + str(ovtPay))

# Calculate/print total pay
totPay = basPay + ovtPay
print('Total Pay:    $' + str(totPay))