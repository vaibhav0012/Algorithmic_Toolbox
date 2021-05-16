# Uses python3
"""Task. Given two non-negative integers 𝑚 and 𝑛, where 𝑚 ≤ 𝑛, find the last digit of the sum 𝐹𝑚 + 𝐹𝑚+1 +
· · · + 𝐹𝑛.
Input Format. The input consists of two non-negative integers 𝑚 and 𝑛 separated by a space.
Constraints. 0 ≤ 𝑚 ≤ 𝑛 ≤ 1014.
Output Format. Output the last digit of 𝐹𝑚 + 𝐹𝑚+1 + · · · + 𝐹𝑛.
Sample 1.
Input:
3 7
Output:
1
𝐹3 + 𝐹4 + 𝐹5 + 𝐹6 + 𝐹7 = 2 + 3 + 5 + 8 + 13 = 31.
Sample 2.
Input:
10 10
Output:
5
𝐹10 = 55.
Sample 3.
Input:
10 200
Output:
2
𝐹10 + 𝐹11 + · · · + 𝐹200 = 734 544 867 157 818 093 234 908 902 110 449 296 423 262
"""
import sys

def fibonacci_partial_sum_naive(n):
    sum = 0
    if n == -1:
        return 0
    if n<=1:
        return n
    previous = 0
    current = 1
    n = (n+2)%60
    for i in range(2,n+1):
        i = i
        previous,current= current,(previous+current)%10
    if(current%10 == 0):
        return 9
    return (current%10-1)


if __name__ == '__main__':
    from_, to = map(int, input().split())
    print((fibonacci_partial_sum_naive(to)-fibonacci_partial_sum_naive(from_-1))%10)
