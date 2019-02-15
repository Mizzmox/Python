import math
import random
while True:
    # Pythagorean theorem follows a strict set when constructing as follows:
    # given any two integers where M < N
    # a = n^2-m^2
    # b = 2nm
    # c = n^2+m^2
    # The result afterwards will satisfy the pythagorean theorem.
    m = random.randint(1, 32)
    n = random.randint(1, 32)
    if(m > n):
        continue
    triangle = []
    leg_one = math.pow(n, 2) - math.pow(m, 2)
    leg_two = 2*m*n
    hypo = math.pow(n, 2) + math.pow(m, 2)
    triangle.append(leg_one)
    triangle.append(leg_two)
    triangle.append(hypo)
    legs = math.pow(triangle[0], 2) + math.pow(triangle[1], 2)
    hypotenuse = math.pow(triangle[2], 2)
    if triangle[0] + triangle[1] + triangle[2] == 1000:
        print("The answer is: " + str(leg_one * leg_two * hypo))
        print("The values of n and m respectively to get this result is " + str(n) + " and " + str(m))
        break
# This program will print the result immediately.    
