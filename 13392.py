import sys
sys.setrecursionlimit(10**6)
n = int(input())
lpre = list(map(int, input()))
lnow = list(map(int, input()))
# dp 잡을 때, dp=[[]*x]*y 하지 말기!
dp = [[-1 for _ in range(10)] for _ in range(n)]

def cal(idx, t):
    if idx == n: return 0
    if dp[idx][t] != -1: return dp[idx][t]
    l = (lnow[idx]-lpre[idx]-t+20)%10
    lmove = cal(idx+1,(t+l)%10)+l
    r = 10-l
    rmove = cal(idx+1, t)+r
    dp[idx][t] = min(lmove, rmove)
    return dp[idx][t]

print(cal(0,0))
print(dp)