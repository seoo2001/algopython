import sys
N = int(sys.stdin.readline())
for _ in range(N):
  a, b = map(int, sys.stdin.readline().split())
  x = a % 10
  l = []
  for _ in range(4):
    l.append(x)
    x = (x*a) % 10
  if l[b%4-1] == 0: print(10)
  else: print(l[b%4-1])