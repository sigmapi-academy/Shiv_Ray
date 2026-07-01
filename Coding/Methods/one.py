# Program to calculate the cost of tent
#
import math 
#  function definition 
def areaOfCyl(h,r):
    area_cyl = 2*math.pi*r*h
    return area_cyl

# Function definition
def areaOfCone(l, r):
    area_con = math.pi*r*l #Area of conical part
    return area_con
    
#  function definition 
def post_tax_price(cost):
    tax = 0.18 * cost
    net_price = cost + tax
    return net_price

def greet(name):
    print(f'Hello! {name}')

def welcome():
    print('*****Welcome to canvas shop*****')
    
def getHeight():
    h = float(input("Height of cylinder: "))
    return h

def getRadius():
    r = float(input(" Enter radius of cylinder: "))
    return r

def getSlantLength():
    l = float(input(" Enter slant height of the conical area in meters : "))
    return l

#  main code
nm = input('Enter your name: ')
greet(nm)
welcome()

h = getHeight()
r = getRadius()
area_of_cylinder = areaOfCyl(h, r)

l = getSlantLength()

concial_area = areaOfCone(l, r)

canvas_area = concial_area + area_of_cylinder
print(f"Area of canvas: {canvas_area:.2f} m^2")

#calculate the cost of canvas
unit_price = float(input("Enter cost of 1m square Canvas in rupees: \u20b9 "))
total_cost = unit_price * canvas_area
print(f"The total cost of canvas before tax equal to \u20B9:{total_cost:.2f}")
print(f"Net amount payable(including tax) = \u20b9 {post_tax_price(total_cost):.2f}")

