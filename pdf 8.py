#Write a program that reads in the radius of a circle and prints the circle‟s diameter,
#circumference and area. Use the constant value 3.14159 for pi. Perform each of these
#calculations inside the print statement(s) and use the conversion format specifier %f.

r = float(input("Enter radius: "))
PI = 3.14159


circum = 2 * PI * r
diameter = 2 * r
area = PI * r * r

print("Circumference:", circum)
print("Diameter:", diameter)
print("Area:", area)