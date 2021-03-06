# Uses python3
"""Task. Given two non-negative integers ๐ and ๐, where ๐ โค ๐, find the last digit of the sum ๐น๐ + ๐น๐+1 +
ยท ยท ยท + ๐น๐.
Input Format. The input consists of two non-negative integers ๐ and ๐ separated by a space.
Constraints. 0 โค ๐ โค ๐ โค 1014.
Output Format. Output the last digit of ๐น๐ + ๐น๐+1 + ยท ยท ยท + ๐น๐.
Sample 1.
Input:
3 7
Output:
1
๐น3 + ๐น4 + ๐น5 + ๐น6 + ๐น7 = 2 + 3 + 5 + 8 + 13 = 31.
Sample 2.
Input:
10 10
Output:
5
๐น10 = 55.
Sample 3.
Input:
10 200
Output:
2
๐น10 + ๐น11 + ยท ยท ยท + ๐น200 = 734 544 867 157 818 093 234 908 902 110 449 296 423 262
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
