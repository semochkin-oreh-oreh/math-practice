import math
from math import pi
area = int(input())
radius = int(input())
def count(a, r):
    circ = 2*pi*r
    per = pow(a, 1/2) * 4
    if (circ > per):
        print("True")
    else:
        print("False")
count(area,radius)
#https://edabit.com/challenge/4me7LifXBwj5rhL4n , Легко

count(16, 16)
count(4, 1)
