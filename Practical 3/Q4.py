"""
Write a Python program which acceptsa sequence of comma separated 5 digit binary numbers as its input and choose the numbers that are divisible by 7 
and add binary 3 to the chosen number and then print in a comma-separated sequence.
Sample Data : 01000,00011,01010,01001,01100,10101Expected Output : 11000
"""


def decimalbinary(n):
    return bin(n).replace("0b","")

list = []
nums = [x for x in input("Enter binary num seperated by comma:").split(',')]

for i in nums:
    x= int(i,2)
    if(x%7 == 0):
        x += 0b0011
        print(decimalbinary(x))