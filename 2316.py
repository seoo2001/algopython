import sys
rl = sys.stdin.readline
N, P = map(int, rl().split())
c = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(P):
    a, b = map(int, rl().split())
    c[a][b], c[b][a] = 1, 1

f = [[0 for _ in range(N+1)] for _ in range(N+1)]
ans = 0
while True:
    q = [1]
    p = [-1 for _ in range(N+1)]
    p[1] = 1
    while q:
        now = q.pop()
        for i in range(1,N+1):
            if c[now][i] - f[now][i]>0 and p[i] == -1:
                q.append(i)
                p[i] = now
    if p[2] == -1: break
    x = 2
    while x != 1:
        f[x][p[x]] -= 1
        f[p[x]][x] += 1
        x = p[x]
    ans += 1
print(ans)