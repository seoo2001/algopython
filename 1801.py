n = int(input())
q = list(map(int, input().split()))
qsum = sum(q)

dp = [[[[0 for _ in range(81)] for _ in range(81)] for _ in range(81)] for _ in range(81)]
dp[0][0][0][0] = 1

for x in q:
    v = []
    for i in range(qsum+1):
        for j in range(i, qsum-i+1):
            for k in range(qsum+1):
                for p in range(k,qsum-k+1):
                    if 2*(j+p)>qsum: continue
                    if dp[i][j][k][p]: continue
                    if i >= x and dp[i-x][j][k][p]: v.append((i,j,k,p))
                    elif j >= x and dp[min(i,j-x)][max(i,j-x)][k][p]: v.append((i,j,k,p))
                    elif k >= x and dp[i][j][min(p,k-x)][max(p,k-x)]: v.append((i,j,k,p))
                    elif p>= x and dp[i][j][min(p-x,k)][max(k,p-x)]: v.append((i,j,k,p))
    for a, b, c, d in v: dp[a][b][c][d] = 1
ans = 0
for i in range(81):
    for j in range(81):
        if dp[i][i][j][j]: ans = max(ans,i*j)

print(ans if ans else -1)

