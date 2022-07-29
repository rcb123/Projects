from time import time
from cmath import sqrt
import math, sys

def sqrt(n, limit):
    floating_point_precision = 10**16
    n_float = float((n * floating_point_precision) // limit) / floating_point_precision
    x = (int(floating_point_precision * math.sqrt(n_float)) * limit) // floating_point_precision
    n_one = n * limit
    while 1:
        x_old = x
        x = (x + n_one // x) // 2
        if x == x_old:
            break
    return x

def chudnovskyPi(limit):
    
    k = 1
    k1 = 545140134
    k2 = 13591409
    k3 = 640320

    a_k = limit
    a_sum = limit
    b_sum = 0

    while 1:
        a_k *= -(6*k-5)*(2*k-1)*(6*k-1)
        a_k //= k*k*k*(k3**3 // 24)
        a_sum += a_k
        b_sum += k * a_k
        k += 1
        if a_k == 0:
            break
    total = k2*a_sum + k1*b_sum
    pi = (426880 * sqrt(10005*limit, limit)*limit) // total
    return pi

def main():
    limit = int(input("Enter the number of decimals to calculate to: "))
    print(chudnovskyPi(10**100))
    for log10_digits in range(1,4):
        digits = 10**log10_digits
        limit = 10**digits

        start =time()
        pi = chudnovskyPi(limit)
        #print(pi)
        print("chudnovsky: digits",digits,"time",time()-start)

if 1==1:
    main()