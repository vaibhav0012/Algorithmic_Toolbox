# Uses python3
"""Task. Compute the last digit of 𝐹2
0 + 𝐹2
1 + · · · + 𝐹2
𝑛.
Input Format. Integer 𝑛.
Constraints. 0 ≤ 𝑛 ≤ 1014.
Output Format. The last digit of 𝐹2
0 + 𝐹2
1 + · · · + 𝐹2
𝑛.
Sample 1.
Input:
7
Output:
3
𝐹2
0 + 𝐹2
1 + · · · + 𝐹2
7 = 0 + 1 + 1 + 4 + 9 + 25 + 64 + 169 = 273.
Sample 2.
Input:
73
Output:
1
𝐹2
0 + · · · + 𝐹2
73 = 1 052 478 208 141 359 608 061 842 155 201.
Sample 3.
Input:
1234567890
Output:
0"""
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    fib = [0, 1]
    sum = 1
    n = n % 60 + 2
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
        #print(fib[i],end = ' ')
    #print()
    out = (fib[n]*fib[n]-fib[n-3]*fib[n-3])//4
    return (out%10)

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_naive(n))
