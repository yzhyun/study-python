import sys
import heapq as hq

sys.stdin = open("../input.txt", "rt")

a = []

while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        if len(a) == 0:
            print("-1")
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, n)