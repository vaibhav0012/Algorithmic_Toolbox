# Uses python3
"""Task. Given an integer π, find the last digit of the πth Fibonacci number πΉπ (that is, πΉπ mod 10).
Input Format. The input consists of a single integer π.
Constraints. 0 β€ π β€ 107.
Output Format. Output the last digit of πΉπ.
Sample 1.
Input:
3
Output:
2
πΉ3 = 2.
Sample 2.
Input:
331
Output:
9
πΉ331 = 668 996 615 388 005 031 531 000 081 241 745 415 306 766 517 246 774 551 964 595 292 186 469."""
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for i in range(1,n):
        new = (previous+current)%10
        previous = current%10
        current = new

    return current

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
