import sys
sys.setrecursionlimit(10**6)
rl = sys.stdin.readline
N, start = map(int, rl().split())
q = [list(map(int, rl().split())) for _ in range(N)]
dp = [[[-1 for _ in range(N)] for _ in range(N)] for _ in range(2)]

qsum = [0 for _ in range(N)]
stemp = 0
for i, x in enumerate(q):
    stemp += x[1]
    qsum[i] = stemp
qsum.insert(0,0)

def cal(s, e, now):
    if dp[now][s][e] != -1: return dp[now][s][e]
    if now==0: nowidx = s
    else: nowidx = e
    if s-1 >= 0: dp[now][s][e] = cal(s-1,e,0)+(q[nowidx][0]-q[s-1][0])*(stemp-qsum[e+1]+qsum[s])
    if e+1 < N:
        if dp[now][s][e] == -1:
            dp[now][s][e] = cal(s,e+1,1)+(q[e+1][0]-q[nowidx][0])*(stemp-qsum[e+1]+qsum[s])
        else: dp[now][s][e] = min(dp[now][s][e], cal(s,e+1,1)+(q[e+1][0]-q[nowidx][0])*(stemp-qsum[e+1]+qsum[s]))
    if dp[now][s][e] == -1: dp[now][s][e] = 0
    return dp[now][s][e]

print(cal(start-1,start-1,0))