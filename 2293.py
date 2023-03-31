n, k = map(int, input().split())
q = [int(input()) for _ in range(n)]
dp = [0 for _ in range(k+1)]
dp[0] = 1
for i in q:
    for j in range(i, k+1):
        dp[j] += dp[j-i]
print(dp[-1])