# Uses python3
"""Task. Given an integer 𝑛, find the last digit of the sum 𝐹0 + 𝐹1 + · · · + 𝐹𝑛.
Input Format. The input consists of a single integer 𝑛.
Constraints. 0 ≤ 𝑛 ≤ 1014.
Output Format. Output the last digit of 𝐹0 + 𝐹1 + · · · + 𝐹𝑛.
Sample 1.
Input:
3
Output:
4
𝐹0 + 𝐹1 + 𝐹2 + 𝐹3 = 0 + 1 + 1 + 2 = 4.
Sample 2.
Input:
100
Output:
5
The sum is equal to 927 372 692 193 078 999 175, the last digit is 5."""

import sys
def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    fib=[0,1]
    sum = 1
    n = n%60+2
    for i in range(2,n+1):
        fib.append(fib[i-1]+fib[i-2])
    if (fib[n]%10==0):
        return (9)
    return ((fib[n] % 10)-1)

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_naive(n))
