"""
 Write a Python program to get a string made of the first 2 and the last 3 chars from a given a string. 
 If the string length is less than 2, return instead the empty string.
 Sample String : "COVID19PANDEMIC" Expected Result : "COMIC"
 Sample String : "CP9" Expected Result: "CPCP9"
 Sample String: "C‟ Expected Result: Empty String
"""

string = str(input("Enter the String : "))

strlen = len(string)

if(strlen < 2):
    print("")
else:
    print(string[:2]+string[-3:])
    