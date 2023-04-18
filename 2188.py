import sys
rl = sys.stdin.readline
N, M = map(int, rl().split())
g = [[] for _ in range(N+1)]
for i in range(N):
    a, *l = map(int, rl().split())
    for x in l: g[i+1].append(x)
slt = [0 for _ in range(M+1)]

def dfs(x):
    for i in g[x]:
        if v[i]: continue
        v[i] = 1
        if slt[i]==0 or dfs(slt[i]):
            slt[i] = x
            return True
    return False

pair = 0
for j in range(1, N+1):
    v = [0 for _ in range(M+1)]
    if dfs(j): pair+=1
print(pair)