import sys
N = int(sys.stdin.readline())

def a(x):
  if case[x] == '1' and x + 3 < caselen:
    if not (case[x+1] == '0' and case[x+2] == '0'): return
    while True:
      if case[x+1] == '0': x += 1
      else: break
    while case[x+1] == '1':
      if x + 1 == caselen - 1:
        ans.append(1)
      a(x+2)
      b(x+2)
      x += 1

def b(x):
  if case[x] == '0' and x + 1 < caselen:
    if case[x+1] == '1':
      if caselen - 1 == x + 1:
        ans.append(1)
        return
      else:
        a(x+2)
        b(x+2)

for _ in range(N):
  ans = []
  case = list(map(str, sys.stdin.readline()))
  case[len(case)-1] = '-1'
  caselen = len(case) - 1
  a(0)
  b(0)
  if ans: print("YES")
  else: print("NO")