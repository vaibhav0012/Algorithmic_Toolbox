# Uses python3
"""Task. Given two integers 𝑛 and 𝑚, output 𝐹𝑛 mod 𝑚 (that is, the remainder of 𝐹𝑛 when divided by 𝑚).
Input Format. The input consists of two integers 𝑛 and 𝑚 given on the same line (separated by a space).
Constraints. 1 ≤ 𝑛 ≤ 1014, 2 ≤ 𝑚 ≤ 103.
Output Format. Output 𝐹𝑛 mod 𝑚.
Sample 1.
Input:
239 1000
Output:
161
𝐹239 mod 1 000 = 39 679 027 332 006 820 581 608 740 953 902 289 877 834 488 152 161 (mod 1 000) = 161.
Sample 2.
Input:
2816213588 239
Output:
151
𝐹2 816 213 588 does not fit into one page of this file, but 𝐹2 816 213 588 mod 239 = 151."""
import sys
def pissano(a):
    previous,current = 0,1
    for i in range(0,m*m):
        previous, current = current, (previous+current)%m
        if(previous ==0 and current ==1):
            return i+1

def get_fibonacci_huge_naive(n, m):
    pissano_num = pissano(m)
    n = n%pissano_num
    if n<=1:
        return n
    previous,current =0,1
    for i in range(n-1):
        previous,current = current,(previous+current)
    return (current%m)

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonacci_huge_naive(n, m))
