# Uses python3
import sys

def gcd(a,b):
    if(b == 0):
        return a
    return (gcd(b, a%b))

def lcm_naive(a, b):
    return ((a*b)//gcd(a,b))

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_naive(a, b))

