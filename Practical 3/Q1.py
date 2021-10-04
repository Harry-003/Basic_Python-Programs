"""
Write a Python program thattakes two digits m (row) and n (column) as input and generates a two-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j*r.
(Value of r is last three digits your Roll no.) 
Note :i = 0,1.., m-1j = 0,1, n-1.r= 80 (if Rollis 18IT080)
Test Data : Rows = 2, Columns =3
Expected Result : [[0, 0, 0],[0, 80, 160]]
"""


m =  int(input("Enter row :"))
n =  int(input("Enter col :"))
r = 37
        
for i in range(0,m):
    for j in range(0,n):
        print(i*j*r,end=" ")
    print()
