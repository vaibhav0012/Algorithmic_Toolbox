# Uses python3
"""Task. Given an integer π, find the last digit of the πth Fibonacci number πΉπ (that is, πΉπ mod 10).
Input Format. The input consists of a single integer π.
Constraints. 0 β€ π β€ 107.
Output Format. Output the last digit of πΉπ

Sample 1.
Input:
10
Output:
55
πΉ10 = 55.
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
