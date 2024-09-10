#This is the assignment for the second quiz

import math

r = input('What is the radius of the desired sphere? ')
r = float(r)

volume_of_sphere = ( 4 / 3 ) * math.pi * (r ** 3)
volume_of_sphere = round(volume_of_sphere, 2)

print('The volume of the desired sphere is ' + str(volume_of_sphere) + ' cube units.')