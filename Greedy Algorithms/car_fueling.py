# python3
"""You are going to travel to another city that is located 𝑑 miles away from your home city. Your car can travel
at most 𝑚 miles on a full tank and you start with a full tank. Along your way, there are gas stations at
distances stop1, stop2, . . . , stop𝑛 from your home city. What is the minimum number of refills needed?
Problem Description
Input Format. The first line contains an integer 𝑑. The second line contains an integer 𝑚. The third line
specifies an integer 𝑛. Finally, the last line contains integers stop1, stop2, . . . , stop𝑛.
Output Format. Assuming that the distance between the cities is 𝑑 miles, a car can travel at most 𝑚 miles
on a full tank, and there are gas stations at distances stop1, stop2, . . . , stop𝑛 along the way, output the
minimum number of refills needed. Assume that the car starts with a full tank. If it is not possible to
reach the destination, output −1.
Constraints. 1 ≤ 𝑑 ≤ 105. 1 ≤ 𝑚 ≤ 400. 1 ≤ 𝑛 ≤ 300. 0 < stop1 < stop2 < · · · < stop𝑛 < 𝑑.
Sample 1.
Input:
950
400
4
200 375 550 750
Output:
2
The distance between the cities is 950, the car can travel at most 400 miles on a full tank. It suffices
to make two refills: at points 375 and 750. This is the minimum number of refills as with a single refill
one would only be able to travel at most 800 miles.
Sample 2.
Input:
10
3
4
1 2 5 9
Output:
-1
One cannot reach the gas station at point 9 as the previous gas station is too far away."""
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    count = 0
    curr =0
    stops.insert(0,0)
    stops.insert(len(stops),distance)
    if (tank>=distance):
        return 0
    while curr <(len(stops)-1):
        prev = curr
        while (curr < len(stops) - 1 and stops[curr + 1] - stops[prev] <= tank):
            diff = stops[curr + 1] - stops[prev]
            curr = curr + 1
        if (distance - stops[curr] <= 0):
            return count
        count = count + 1
        if (curr < len(stops) - 1 and stops[curr + 1] - stops[curr] > tank):
            return -1
        if (curr == len(stops) - 2 and distance - stops[curr + 1] < tank):
            return count
    return count

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
