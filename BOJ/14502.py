import sys
from itertools import combinations
rl = sys.stdin.readline
n, m = map(int, rl().split())
graph = [list(map(int, rl().split())) for _ in range(n)]
case = []
dr = [(0,1), (0,-1), (1,0), (-1,0)]
visited = [[0 for _ in range(m)] for _ in range(n)]
out = 0
twocheck = False
def sol(c):
  global visited, out, twocheck
  visited = [[0 for _ in range(m)] for _ in range(n)]
  solout = 0
  for w in c: graph[case[w][1]][case[w][0]] = 1
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0 and visited[i][j] == 0:
        out = 0
        dfs(j, i)
        if not twocheck:
          solout += out
        twocheck = False
  for w in c: graph[case[w][1]][case[w][0]] = 0    
  return solout

def dfs(x, y):
  global visited, out, twocheck
  visited[y][x] = 1
  out += 1
  for dx, dy in dr:
    if 0<=x+dx<m and 0<=y+dy<n:
      if graph[y+dy][x+dx] == 2: twocheck = True
      if graph[y+dy][x+dx] == 0 and visited[y+dy][x+dx] == 0:
        dfs(x+dx, y+dy)

for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      case.append([j, i])
comb = list(combinations([x for x in range(len(case))], 3))
ans = 0
for c in comb: ans = max(ans, sol(c))
print(ans)