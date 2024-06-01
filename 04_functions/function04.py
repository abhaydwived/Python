import math
radius=int(input("Enter radius..."))
def circle(radius):
    area=(math.pi*radius**2)
    circumference=(2*math.pi*radius)
    return area,circumference
a,c=circle(radius)
print("Area:",a,"circumference:",c)
