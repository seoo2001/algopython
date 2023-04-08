import sys
from collections import deque
rl = sys.stdin.readline
N, L = map(int, rl().split())
nums = list(map(int, rl().split()))
q = deque()
for i, x in enumerate(nums):    
    if q:
        xTemp, iTemp = q[0]
        if iTemp < i-L+1: q.popleft()
    while q:
        xTemp, iTemp = q[-1]
        if xTemp > x: q.pop()
        else: break
    q.append([x,i])
    print(q[0][0])