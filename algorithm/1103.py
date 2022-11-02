import sys
rl = sys.stdin.readline
n, m = map(int, rl().split())
graph = [[] for _ in range(n)]
for i in range(n): 
  g = list(rl().rstrip())
  for x in g:
    if x.isdigit(): graph[i].append(int(x))
    else: graph[i].append(x)
dr = [(1,0),(-1,0),(0,1),(0,-1)]



def move(x, y):
  if x<0 or x>=m or y<0 or y>=n: return 0
  if graph[y][x] == "H": return 0
  return 1
visit = [[0 for _ in range(m)] for _ in range(n)]
q = [[0, 0, 0, {(0,0)}]]
ans = 0
breaker = False
while q and not breaker:
  x, y, k, vset = q.pop()
  vset = set(vset)
  visit[y][x] = k
  ans = max(ans, k)
  for ddx, ddy in dr:
    dx = ddx*graph[y][x]
    dy = ddy*graph[y][x]
    if move(x+dx, y+dy):
      if visit[y+dy][x+dx] < k+1:
        if (x+dx, y+dy) in vset:
          print(-1)
          breaker = True
        else:
          vset.add((x+dx, y+dy))
          t = vset.copy()
          q.append([x+dx, y+dy, k+1, t])
          vset.remove((x+dx, y+dy))
if not breaker: print(ans+1)
  