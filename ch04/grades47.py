'''
Created on Jan 10, 2019
This program accepts a score between 0.0 and 1.0, inclusive, 
and prints out a corresponding grade. Bad input is flagged.
@author: ebrie
'''

def computegrade(score):
    if score > 1.0 or score < 0.0:
        return "Bad score"
    elif score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        return "F"
    
s = input("Enter score (0.0-1.0)?")
try:
    score = float(s)
except:
    score = 999
    
grade = computegrade(score)
print("Grade = " + grade)