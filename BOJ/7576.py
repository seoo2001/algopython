import sys
from collections import deque
rl = sys.stdin.readline
col, row = map(int, rl().split())
graph = [list(map(int, rl().split())) for _ in range(row)]
dr = [(1,0), (-1,0), (0,1), (0,-1)]
q = deque()
visited = [[0 for _ in range(col)] for _ in range(row)]
out = 0
for i in range(col):
  for j in range(row):
    if graph[j][i] == 1:
      q.appendleft([1, i, j])
      visited[j][i] = 1

while q:
  c, x, y = q.pop()
  for dx, dy in dr:
    if 0<=y+dy<row and 0<=x+dx<col:
      if graph[y+dy][x+dx] == 0 and visited[y+dy][x+dx] == 0:
        q.appendleft([c+1, x+dx, y+dy])
        graph[y+dy][x+dx] = c + 1
        visited[y+dy][x+dx] = 1
  out = c

breaker = False
for g in graph:
  for i in g:
    if i == 0: breaker = True
if breaker == False: print(c-1)
else: print(-1)