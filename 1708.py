import sys
rl = sys.stdin.readline
MAXD = 16
N = int(rl())
g = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, rl().split())
    g[a].append([b,c])
    g[b].append([a,c])

p =[[[0,0] for _ in range(MAXD)] for _ in range(N+1)]
dpt = [0 for _ in range(N+1)]
dpt[1] = 1
q = [[1,1]]
while q:
    x, d = q.pop()
    for nx, w in g[x]:
        if not dpt[nx]:
            q.append([nx, d+1])
            dpt[nx] = d+1
            p[nx][0] = [x, w]

for j in range(1,MAXD):
    for i in range(1,N+1):
        p[i][j][0] = p[p[i][j-1][0]][j-1][0]
        p[i][j][1] = p[i][j-1][1] + p[p[i][j-1][0]][j-1][1]

def LCA(x,y):
    out = 0
    if dpt[x] > dpt[y]:x,y=y,x
    for i in range(MAXD, -1, -1):
        if dpt[y] - dpt[x] >= (1<<i):
            out += p[y][i][1]
            y = p[y][i][0]
    if x==y: return out
    for i in range(MAXD-1,-1,-1):
        if p[x][i][0] != p[y][i][0]:
            out = out+p[x][i][1]+p[y][i][1]
            x = p[x][i][0]
            y = p[y][i][0]
    out = out+p[x][0][1]+p[y][0][1]
    return out

M = int(rl())
for _ in range(M):
    a, b = map(int, rl().split())
    print(LCA(a,b))