# Uses python3
"""Task. Given an integer 𝑛, find the last digit of the 𝑛th Fibonacci number 𝐹𝑛 (that is, 𝐹𝑛 mod 10).
Input Format. The input consists of a single integer 𝑛.
Constraints. 0 ≤ 𝑛 ≤ 107.
Output Format. Output the last digit of 𝐹𝑛

Sample 1.
Input:
10
Output:
55
𝐹10 = 55.
"""


def calc_fib(n):
    if n<=1:
        return n
    arr = [0,1]
    for i in range(2,n+1):
        arr.append(arr[i-1]+arr[i-2])

    return (arr[n])

n = int(input())
print(calc_fib(n))
