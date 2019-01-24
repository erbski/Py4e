'''
Created on Jan 23, 2019

@author: ebrie
'''
total = 0
count = 0
lowest = None
highest = None
while True:
    line = input('>>> ')
    if line == "done":
        break
    try:
        nbr = int(line)
    except:
        print("Not numeric. Try again.")
        continue
    total = total + nbr
    count = count + 1
    if highest is None or nbr > highest:
        highest = nbr
    if lowest is None or nbr < lowest:
        lowest = nbr
        
print("Input count = ", count)
print("Input sum = ", total)
if count > 0:
    print("Input avg = ", total / count)
print("Lowest number = ", lowest)
print("Highest number = ", highest)
