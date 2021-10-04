m= int(input("Enter no. of rows: "))
n = int(input("Enter no. of columns: "))
r = int(input("Enter your ID number: "))

matrix = [[0 for col in range(m)]for row in range(n)]
for i in range(m):
    for j in range(n):
        matrix[i][j]=i*j*r

print(matrix)