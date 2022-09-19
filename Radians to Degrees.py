import math
from math import pi
eps = 1e-7
rad = int(input())
def radians_to_degrees(r):
    deg = (180/pi) * r
    return deg

#https://edabit.com/challenge/2X2uZysLJ3CpsxLDD , Легко

def test(rad, deg):
    if (abs(180/pi) * rad - deg) < eps:
        print("passed")
    else:
        print("error")
test(rad, radians_to_degrees(rad))
test(3, 171.88733853924)
test(5, 286.478897565)

