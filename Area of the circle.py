import math
#Create a Python program that computes the area of a circle

def area_of_circle(radius):
    area_of_circle = 3.141592653589793238 * radius * radius
    return area_of_circle

radius = int(input("Enter the value of radius:"))
print("The area of the circle is: ", area_of_circle(radius))
