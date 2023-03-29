import sys
sys.setrecursionlimit(10**6)
rl = sys.stdin.readline
n = int(rl())
qs = [list(map(int, rl().split())) for _ in range(n)]
dp = [[-1 for _ in range(1001)] for _ in range(1001)]
visit = [0 for _ in range(n)]
qs.sort()
def cal(ss, ii):
    if (ss >= 1000 or ii >= 1000): return 51
    if dp[ss][ii] != -1: return dp[ss][ii]
    dp[ss][ii] = 0
    v, t = [], 0
    for i in range(n):
        if visit[i] == 0 and (qs[i][0] <= ss or qs[i][1] <= ii):
            visit[i] = 1
            v.append(i)
            t += qs[i][2]
    for i in range(t+1):
        dp[ss][ii] = max(dp[ss][ii], cal(ss+i, ii+t-i)+len(v))
    for x in v: visit[x] = 0
    return dp[ss][ii]

ans = cal(1,1)
if ans > n: print(n)
else: print(ans)