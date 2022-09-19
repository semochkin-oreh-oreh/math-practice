import math
from math import pi
num = int(input())
flag = input()
def count(l, f):
    res = -1
    if f == "s":
        res = 4*l
    if f == "c":
        res = 2*pi*l
    return res
print(count(num, flag))
# https://edabit.com/challenge/WEvqZTFcHeYzFn74c , Средне
def test(n, f):
    if ((f == "s") or (f == "c")) == 0:
        print("error")
    if n < 0:
        print("error")
test(3, "u")
test(-2, "s")
