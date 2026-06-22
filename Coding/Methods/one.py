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

#  main code
h = float(input("Height of cylinder: "))
r = float(input(" Enter radius of cylinder: "))
area_of_cylinder = areaOfCyl(h, r)

l = float(input(" Enter slant height of the conical area in meters : "))
concial_area = areaOfCone(l, r)

canvas_area = concial_area + area_of_cylinder
print(f"Area of canvas: {canvas_area:.2f} m^2")

#calculate the cost of canvas
unit_price = float(input(" Inter cost of 1m square Canvas in rupees: \u20b9 "))
total_cost = unit_price * canvas_area
print(f"The total cost of canvas before tax equal to \u20B9:{total_cost:.2f}")
print(f"Net amount payable(including tax) = \u20b9 {post_tax_price(total_cost):.2f}")

