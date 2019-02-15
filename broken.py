import math
import random
while True:
    triangle = []
    leg_one = random.randint(1, 500)
    leg_two = random.randint(1, 500)
    hypo = random.randint(1, 500)
    triangle.append(leg_one)
    triangle.append(leg_two)
    triangle.append(hypo)
    legs = math.pow(triangle[0], 2) + math.pow(triangle[1], 2)
    hypotenuse = math.pow(triangle[2], 2)
    if legs == hypotenuse and triangle[0] + triangle[1] + triangle[2] == 1000:
        print triangle
        break
something = input("placeholder")    
