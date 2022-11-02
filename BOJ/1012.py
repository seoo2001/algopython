import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
dr = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(x, y):
  if graph[y][x] == 0: return
  graph[y][x] = 0
  for dx, dy in dr:
    dfs(x+dx, y+dy)  

for _ in range(N):
  m, n, k = map(int, sys.stdin.readline().split())
  pos = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]
  graph = [[0 for _ in range(m+2)] for _ in range(n+2)]
  for x, y in pos:
    graph[y+1][x+1] = 1
  ans = 0
  for i in range(1, n+1):
    for j in range(1, m+1):
      if graph[i][j] == 1:
        ans += 1
        dfs(j, i)
  print(ans)