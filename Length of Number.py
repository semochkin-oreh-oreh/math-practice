import math
num = int(input())
def dec(n):
    count = 1
    while n > 0:
        n = n//10
        if n > 0:
            count += 1
    return count

#https://edabit.com/challenge/2zKetgAJp4WRFXiDT , Средний

def test(N, c):
    if N//pow(c, 10) == 0:
        print("passed")
    else:
        print("error")
test(num, dec(num))
test(0, 1)
test(12345600, 8)
