import sys
from collections import deque
rl = sys.stdin.readline
N = int(rl())
g = [[] for _ in range(N+1)]
MAXDEPTH = 17
for _ in range(N-1):
    a, b, c = map(int, rl().split())
    g[a].append([b,c])
    g[b].append([a,c])
par = [[[0,0,0] for _ in range(MAXDEPTH)] for _ in range(N+1)] #par, min, max
dpt = [0 for _ in range(N+1)]
vali = [[1e9,0] for _ in range(N+1)]
q = deque([(1,1)])
dpt[1] = 1
while q:
    x, d = q.popleft()
    for nx, w in g[x]:
        if not dpt[nx]:
            q.append((nx, d + 1))
            dpt[nx] = d + 1
            par[nx][0] = [x,w,w]


for j in range(1,MAXDEPTH):
    for i in range(1,N+1):
        par[i][j][0] = par[par[i][j-1][0]][j-1][0]
        par[i][j][1] = min(par[i][j-1][1], par[par[i][j-1][0]][j-1][1])
        par[i][j][2] = max(par[i][j-1][2], par[par[i][j-1][0]][j-1][2])

def LCA(x,y):
    minval, maxval = 1e9,0
    if dpt[x] > dpt[y]: x,y=y,x
    for i in range(MAXDEPTH,-1,-1):
        if dpt[y] - dpt[x] >= (1<<i):
            minval = min(minval, par[y][i][1])
            maxval = max(maxval, par[y][i][2])
            y = par[y][i][0]
    if x==y: return [minval, maxval]
    for i in range(MAXDEPTH-1,-1,-1):
        if par[x][i][0] != par[y][i][0]:
            minval = min(minval, par[x][i][1],par[y][i][1])
            maxval = max(maxval, par[x][i][2],par[y][i][2])
            x = par[x][i][0]
            y = par[y][i][0]
    minval = min(minval, par[x][0][1],par[y][0][1])
    maxval = max(maxval, par[x][0][2],par[y][0][2])
    return [minval,maxval]

K = int(rl())
for _ in range(K):
    d, e = map(int, rl().split())
    print(*LCA(d,e))