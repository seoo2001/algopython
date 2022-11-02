import sys, copy
rl = sys.stdin.readline

n, m = map(int, rl().split())
graph = [list(map(int, rl().rstrip())) for _ in range(n)]
d = [(1,1),(1,-1),(-1,1),(-1,-1)] # rd, ru, ld, lu
gh = [copy.deepcopy(graph) for _ in range(4)]

def sum(x, y, dr):
  global gh
  for i in range(1, max(n,m)):
    if 0<= x+i*d[dr][0] < m and 0 <= y+i*d[dr][1] < n:
      if graph[y+i*d[dr][1]][x+i*d[dr][0]] == 1:
        gh[dr][y+i*d[dr][1]][x+i*d[dr][0]] += gh[dr][y+(i-1)*d[dr][1]][x+(i-1)*d[dr][0]]
    else: break

for i in range(n):
  sum(0, i, 0)
  sum(0, i, 1)
  sum(m-1, i, 2)
  sum(m-1, i, 3)
for i in range(1, m-1):
  sum(i, 0, 0)
  sum(i, 0, 2)
  sum(i, n-1, 1)
  sum(i, n-1, 3)
# rd, ru, ld, lu
ans = 0
for y in range(n):
  for x in range(m):
    if min(gh[3][y][x], gh[2][y][x]) <= ans: continue
    for t in range(1, min(gh[3][y][x], gh[2][y][x])+1):
      if 0 <= x+t*2-2 < m:
        if gh[1][y][x+t*2-2] >= t and gh[0][y][x+t*2-2] >= t:
          ans = max(ans, t)
print(ans)