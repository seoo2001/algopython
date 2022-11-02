import sys
from itertools import combinations

N = int(sys.stdin.readline())

for _ in range(N):
  nodeNum = int(sys.stdin.readline())
  nodepos = [list(map(int, sys.stdin.readline().split())) for _ in range(nodeNum)]
  answer = []
  combs = list(combinations(range(nodeNum), nodeNum//2))
  for comb in combs:
    ansx, ansy = 0, 0
    for n in range(nodeNum):
      if n in comb:
        ansx, ansy = ansx + nodepos[n][0], ansy + nodepos[n][1]
      else:
        ansx, ansy = ansx - nodepos[n][0], ansy - nodepos[n][1]
    answer.append((ansx**2+ansy**2)**0.5)
  print(min(answer))