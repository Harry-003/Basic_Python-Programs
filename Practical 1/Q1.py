"""
Write Python Program (WPP) to enter length and breadth of a rectangle and calculate area and perimeter of the rectangle. 

"""

length = int(input("Enter length of rectangle : "))
width = int(input("Enter width of rectangle : "))

print("Area of Rectangle : ",length*width)
print("Perimeter of Rectangle : ",2*(length + width))