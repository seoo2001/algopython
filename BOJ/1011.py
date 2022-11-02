import sys
N = int(sys.stdin.readline())
for _ in range(N):
  n, m = map(int, sys.stdin.readline().split())
  dis = m-n
  cnt = 0
  move = 1
  movesum = 0
  while movesum < dis:
    cnt += 1
    movesum += move
    if cnt % 2 == 0: move += 1
  print(cnt)