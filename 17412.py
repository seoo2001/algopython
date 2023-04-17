import sys
rl = sys.stdin.readline
N, P = map(int, rl().split())
c = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(P):
    a, b = map(int, rl().split())
    c[a][b] = 1

flow = [[0 for _ in range(N+1)] for _ in range(N+1)]
ans=0 
while True:
    p = [-1 for _ in range(N+1)]
    q = [1]
    while (q and p[2]==-1):
        now = q.pop()
        for i in range(1,N+1):
            if c[now][i]-flow[now][i]>0 and p[i]==-1:
                q.append(i)
                p[i] = now
    if p[2] == -1: break
    amount = 1e9
    x = 2
    while x != 1:
        amount = min(c[p[x]][x]-flow[p[x]][x], amount)
        x = p[x]
    x = 2
    while x!= 1:
        flow[p[x]][x] += amount
        flow[x][p[x]] -= amount
        x = p[x]
    ans += amount
print(ans)