import sys, copy
rl = sys.stdin.readline
n, m = map(int, rl().split())
graph = [list(rl().rstrip()) for _ in range(n)]
rx, ry, bx, by = 0,0,0,0
holex, holey = 0,0
for i in range(n):
  for j in range(m):
    if graph[i][j] == "B": 
      graph[i][j] = "."
      bx,by=j,i
    if graph[i][j] == "R":
      graph[i][j] = "."
      rx,ry=j,i
    if graph[i][j] == "O": holex, holey = j,i

def move(x, y, r, g):
  nextx, nexty = x, y
  if r == 0: nextx = ''.join(g[y]).find("#", x)-1 #right
  elif r == 1: nextx = ''.join(g[y]).rfind("#", 0, x)+1 #left
  elif r == 2: nexty = ''.join([i[x] for i in g]).find("#", y)-1 #down
  elif r == 3: nexty = ''.join([i[x] for i in g]).rfind("#",0,y)+1 #up
  if holey == y and holex in range(min(x,nextx),max(x,nextx)+1): return -1,-1
  if holex == x and holey in range(min(y,nexty),max(y,nexty)+1): return -1,-1
  return nextx, nexty

def rbmove(rx, ry, bx, by, i):
  global graph
  graph[by][bx] = "#"
  nextrx, nextry = move(rx,ry,i,graph)
  graph[nextry][nextrx] = "#"
  graph[by][bx] = "."
  nextbx, nextby = move(bx,by,i,graph)
  graph[nextry][nextrx] = "."  
  return nextrx, nextry, nextbx, nextby

breaker = False
q = [[rx, ry, bx, by]]
visited = [[[[0 for _ in range(10)] for _ in range(10)] for _ in range(10)] for _ in range(10)]
visited[rx][ry][bx][by] = 1

for cnt in range(11):
  if breaker == True:
    print(cnt)
    break
  nq = []
  while q:
    # print(q)
    rx, ry, bx, by = q.pop()
    for i in range(4):
      if i == 0:
        if rx > bx: nrx, nry, nbx, nby = rbmove(rx,ry,bx,by, i)
        else: nbx, nby, nrx, nry = rbmove(bx,by,rx,ry, i)
      elif i == 1:
        if rx < bx: nrx, nry, nbx, nby = rbmove(rx,ry,bx,by, i)
        else: nbx, nby, nrx, nry = rbmove(bx,by,rx,ry, i)
      elif i == 2:
        if ry > by: nrx, nry, nbx, nby = rbmove(rx,ry,bx,by, i)
        else: nbx, nby, nrx, nry = rbmove(bx,by,rx,ry, i)
      elif i == 3:
        if ry < by: nrx, nry, nbx, nby = rbmove(rx,ry,bx,by, i)
        else: nbx, nby, nrx, nry = rbmove(bx,by,rx,ry, i)
      if nrx == -1: 
        if nby != -1: breaker = True
        else: nrx, nry, nbx, nby = rx, ry, bx, by
      if nby == -1: nrx, nry, nbx, nby = rx, ry, bx, by
      if visited[nrx][nry][nbx][nby] == 0:
        visited[nrx][nry][nbx][nby] = 1
        nq.append([nrx, nry, nbx, nby])
  q = copy.deepcopy(nq)
  # print(nq)
else: print(-1)