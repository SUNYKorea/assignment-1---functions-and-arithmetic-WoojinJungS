# Name: Woojin Jung
# SBUID:  115964091
##################### SCORE ######################
####### Score:  2/10
#################################################
# Remove the ellipses (...) when writing your solutions.
# your output:
# (base) D:\CSE 101 Ass1\Assignment 1 - Functions and Arithmetic-04-05-2023-05-19-27>D:/anaconda/python.exe "d:/CSE 101 Ass1/Assignment 1 - Functions and Arithmetic-04-05-2023-05-19-27/WoojinJungS/Homework_1.py"
# wear Sweater!! --> correct
# The area of the triangle is : 2.0 , its perimeter is : 19.559919750220082 -> wrong
# The area of the polygon is : -3.8979678309048262-> wrong
# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

def fahrenheit2celsius(fahrenheit): 
   return (5/9) * (fahrenheit - 32)

def what_to_wear(celsius):
    if celsius < - 10:
        print("wear PuffyJacket!!")
    elif -10 < celsius < 0:
        print("wear Scarf!!")
    elif 0 < celsius < 10:
        print("wear Sweater!!")
    elif 10 < celsius < 20:
        print("wear LightJacket!!")
    elif 20 < celsius:
        print("wear T-shirt!!")
    else:
        print("I'm in a dilemma between two options!!")

#It is a void function
#values of -10, 0, 10, 20 intentionally left for else, since it is not specified in assignment

# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    return abs(((x1 + x2 + x3) - (y1 + y2 + y3))/2)

def euclidean_distance(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 + y2)**2) ** 0.5

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    return sum((euclidean_distance(x1, y1, x2, y2), euclidean_distance(x1, y1, x3, y3), euclidean_distance(x2, y2, x3, y3)))



# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 

import math

def deg2rad(deg):
    return math.radians(deg)

def apothem(number_sides, length_side):
    return length_side / (2 * math.tan(180 / deg2rad(number_sides)))

def polygon_area(number_sides, length_side):
    return number_sides * length_side * apothem(number_sides, length_side) / 2 


# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
fahrenheit = 40
what_to_wear(fahrenheit2celsius(fahrenheit))

# Exercise 2 test
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))

