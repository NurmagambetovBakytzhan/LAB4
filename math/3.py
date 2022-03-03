from math import *
sides = float(input("number of sides: "))
length_side = float(input("the length of a side: "))
apothem = ( length_side/(2* tan((pi/sides) )))
print(f"The area of the polygon is: {int(sides * length_side * apothem * 0.5)}")