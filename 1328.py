n, l, r = map(int, input().split())
dp = [[[0]*101 for _ in range(101)] for _ in range(101)]
dp[1][1][1] = 1
for i in range(2, n+1):
    dp[i][1][i], dp[i][i][1] = 1, 1
    for j in range(1, i+1):
        for k in range(1, i+1):
            dp[i][j][k] = (dp[i-1][j-1][k]+dp[i-1][j][k-1]+dp[i-1][j][k]*(i-2))%1000000007
print(dp[n][l][r])