'''
Created on Jan 10, 2019
This program accepts a score between 0.0 and 1.0, inclusive, 
and prints out a corresponding grade. Bad input is flagged.
@author: ebrie
'''
s = input("Enter score (0.0-1.0)?")
try:
    score = float(s)
except:
    score = 999
    
if score > 1.0 or score < 0.0:
    grade = "Bad score"
elif score >= 0.9:
    grade = "A"
elif score >= 0.8:
    grade = "B"
elif score >= 0.7:
    grade = "C"
elif score >= 0.6:
    grade = "D"
else:
    grade = "F"
    
print("Grade = " + grade)