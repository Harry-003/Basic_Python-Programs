'''
Demonstrate the Python Exception with following concepts
try
except
else
finally
'''
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

try:
    result = num1 / num2
except:
    print("Number cannot be divided by 0")
else:
    print(f"{num1} divided by {num2} is {result}")
finally:
    print("Have a nice day")