import sys
import copy
rl = sys.stdin.readline
n, m, a, b, k = map(int, rl().split())
g = [[0 for _ in range(m+2)] for _ in range(n+2)]
for i in range(n+2):
  g[i][0] = 1
  g[i][m+1] = 1
for i in range(m+2):
  g[0][i] = 1
  g[n+1][i] = 1
for _ in range(k):
  x, y = map(int, rl().split())
  g[x][y] = 1
startx, starty = map(int, rl().split())
endx, endy = map(int, rl().split())

dp = [[0 for _ in range(n+2)] for _ in range(m+2)]
dr = [(1,0,a-1),(-1,0,0),(0,1,b-1),(0,-1,0)]
q = [[startx, starty, 0]]
ans = -1
while q:
  q2 = []
  for x, y, k in q:
    dp[x][y] = 1
    if x == endx and y == endy: 
      ans = k
      break
    for dx,dy,dw in dr:
      if dp[x+dx][y+dy] == 0:
        if dy == 0:
          for i in range(b):
            if g[x+dx+dw][y+dy+i] == 1: break
          else: q2.append([x+dx,y+dy,k+1])
        else:
          for i in range(a):
            if g[x+dx+i][y+dy+dw] == 1: break
          else: q2.append([x+dx,y+dy,k+1])
  q = copy.deepcopy(q2)
print(ans)