from re import X
import sys
from heapq import heappush, heappop
rl = sys.stdin.readline
n = int(rl())
rheap, lheap = [], []
for i in range(n):
  x = int(rl())
  if len(lheap) == len(rheap):
    heappush(lheap, (-x, x))
  else: heappush(rheap, (x, x))
  if rheap:
    if lheap[0][1] > rheap[0][1]:
      x, y = heappop(lheap)
      heappush(rheap, (x, y))
      x, y = heappop(rheap)
      heappush(lheap, (-x , y))
  print(lheap[0][1])