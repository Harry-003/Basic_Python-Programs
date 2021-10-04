"""
Write a Python program which iterates the integers from 1 to 100.
 For multiples of 6 print "CHARUSAT" instead of the number and for the multiples of 4 print "IT". 
For numbers which are multiples of both 4 and 6 print "CHARUSAT_IT"
"""


for i in range(0,100):
    if(i%6 == 0):
        print("CHARUSAT")
    if(i%4 == 0):
        print("IT")
    if(i%6 == 0 and i%4 == 0):
        print("CHARUSAT_IT")
