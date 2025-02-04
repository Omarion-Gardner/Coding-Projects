#Omarion Gardner
#Project 3
#1 hour and 30 minutes
#9/20/2023
#import math
import math
#Create a function to welcome the user
def welcome():
    welcome= """Welcome to my Garden Plot Calculator
Note, all calculations are in feet"""
    return welcome

#Create a function that prompts the user for length of one side of garden to find the total square footage of the garden
def length(a):
    a= a**2
    length = a
    return length
#Create a function that prompts the user to enter the radius of the fountain to find the square footage of the fountain
def radius(b):
    b= math.pi*b**2
    radius = b
    return radius
#Create a function that prompts the user to enter the depth of the flower bed to find the amount of soil needed
def depth(c):
    depth = c
    return depth
def soil(d):
    soil = depth(c)*(length(a)-radius(b))
    return soil
def main():
    print(welcome())
    a = float(input("Please enter the length of one of the sides of the garden: "))
    print("You entered", a)
    b = float(input("Please enter the radius of the fountain: "))
    print("You entered", b)
    c = float(input("Please enter the depth of the flower bed: "))
    print("You entered", c)
    #Calculates the total square footage of the garden
    garden = round(length(a),1)
    #Calculates the square footage of the fountain
    fountain = round(radius(b),1)
    #Calculates the square footage of the flower bed
    flower = garden - fountain
    #Calculates the amount of soil needed
    soil = flower * depth(c)
    soil2 = round(soil,1)
    #Gives the user the results
    print("The total square footage of the garden is ",garden)
    print("The square footage of the fountain is ",fountain)
    print("The square footage of the flower bed is ",flower)
    print("The flower bed needs",soil2,"cubic feet of soil")

if __name__=="__main__":
    main()    
