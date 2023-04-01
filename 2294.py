import sys
rl = sys.stdin.readline
n, k = map(int, input().split())
q = [int(input()) for _ in range(n)]
dp = [1e9 for _ in range(k+1)]
dp[0] = 0

for x in q:
    for i in range(x, k+1):
        dp[i] = min(dp[i], dp[i-x]+1)
print(dp[-1] if dp[-1]!=1e9 else -1)