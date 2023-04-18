import sys
rl = sys.stdin.readline
N, P = map(int, rl().split())
MN = N*2+2
c = [[0 for _ in range(MN)] for _ in range(MN)]
for i in range(2,MN,2): c[i][i+1] = 1
c[2][3], c[4][5] = 1e9, 1e9
for _ in range(P):
    a, b = map(int, rl().split())
    c[a*2+1][b*2], c[b*2+1][a*2] = 1, 1

f = [[0 for _ in range(MN)] for _ in range(MN)]
ans = 0
while True:
    q = [2]
    p = [-1 for _ in range(MN)]
    p[2] = 2
    while q:
        now = q.pop()
        for i in range(1,MN):
            if c[now][i] - f[now][i]>0 and p[i] == -1:
                q.append(i)
                p[i] = now
    if p[5] == -1: break
    x = 5
    while x != 2:
        f[x][p[x]] -= 1
        f[p[x]][x] += 1
        x = p[x]
    ans += 1
print(ans)