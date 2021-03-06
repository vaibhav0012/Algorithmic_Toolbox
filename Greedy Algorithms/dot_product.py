#Uses python3
"""Task. Given two sequences ๐1, ๐2, . . . , ๐๐ (๐๐ is the profit per click of the ๐-th ad) and ๐1, ๐2, . . . , ๐๐ (๐๐ is
the average number of clicks per day of the ๐-th slot), we need to partition them into ๐ pairs (๐๐, ๐๐)
such that the sum of their products is maximized.
Input Format. The first line contains an integer ๐, the second one contains a sequence of integers
๐1, ๐2, . . . , ๐๐, the third one contains a sequence of integers ๐1, ๐2, . . . , ๐๐.
Constraints. 1 โค ๐ โค 103; โ105 โค ๐๐, ๐๐ โค 105 for all 1 โค ๐ โค ๐.
Output Format. Output the maximum value of
ฮฃ๏ธ๐
๐=1
๐๐๐๐, where ๐1, ๐2, . . . , ๐๐ is a permutation of
๐1, ๐2, . . . , ๐๐.
Sample 1.
Input:
1
23
39
Output:
897
897 = 23 ยท 39.
Sample 2.
Input:
3
1 3 -5
-2 4 1
Output:
23
23 = 3 ยท 4 + 1 ยท 1 + (โ5) ยท (โ2)."""
import sys

def max_dot_product(a, b):
    #write your code here
    res = 0
    a = sorted(a)
    b = sorted(b)
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
