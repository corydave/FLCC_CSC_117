import math

def test():
    print('circle_util is working')

def area(r):
    circle_area = math.pi * r * r
    print(f'The area is {circle_area}')

def circumference(radius):
    circle_circumference = 2 * math.pi * radius
    print(f'The circumference is {circle_circumference}')
