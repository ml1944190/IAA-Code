# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Implementation of Algorithm 6.3 - Rabin-Miller
## Ryan McIntyre
## 12/12/2016
## python 3.5.2

from random import choice
from copy import copy
import sys

def RabinMiller(n,iterations=20):
    if n == 2:
        print(n,'IS prime.')
        return True
    if n%2 == 0:
        print(n,'is NOT prime.')
        return False
    i = 0
    while i < iterations:
        if not RabinMillerCore(n):
            print(n,'is NOT prime.')
            return False
        i += 1
    print(n,'IS prime.')
    return True
    
def RabinMillerCore(n):
    a = choice(range(2,n-1))
    if exp(a,n-1,n) != 1:
        return False
    s = n-1
    h = 0
    while s%2 == 0:
        s /= 2
        h += 1
    s = int(s)
    h = int(h)
    x = exp(a,s,n)
    if x==1 or x == n-1:
        return True
    i = 0
    last = 0
    while i < h:
        last = copy(x)
        x = exp(x,2,n)
        if x == 1:
            if last == n-1:
                return True
            else:
                return False
        i += 1
    print('The impossible has happened...')
    return False
    
def exp(a,n,m):#a^n mod m (a^n if m==0)
    nB = "{0:b}".format(int(n))
    A = [a]
    i = 1
    while i < len(nB):
        new = A[i-1]**2
        new = new%m
        A.append(new)
        i += 1
    i = 1
    output = 1
    while i <= len(nB):
        if int(nB[-i]) == 1:
            output *= A[i-1]
            output = output%m
        i += 1
    return output

if __name__ == '__main__':
    n = len(sys.argv)
    if n < 2:
        raise TypeError('Rabin-Miller requires a postive integer input.')
    elif n > 3:
        raise TypeError('Got 3 inputs for Rabin-Miller. Expected at most 2.')
    elif n==3:
        RabinMiller(int(sys.argv[1]),int(sys.argv[2]))
    else:
        RabinMiller(int(sys.argv[1]))