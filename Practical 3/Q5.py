"""
Write a Python program that accepts a string and calculate the number of digits and letters.
Sample Data: “Unlock 3.0 is about to release” 
Expected Output: Letters: 22 Digits: 2

"""


str = input("Enter String : ")

char = 0
digit = 0

for i in str:
    if i.isalpha():
        char+= 1
    else:
        digit+= 1

print("Num of character in given string : ",char)
print("Num of digits in given string : ",digit)