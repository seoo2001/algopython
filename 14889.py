from itertools import combinations
N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]
ans = 1e9

def cal(left, right):
    global ans
    a, b = 0, 0
    for i in range(N//2):
        for j in range(i,N//2):
            a = a+m[left[i]][left[j]]+m[left[j]][left[i]]
            b = b+m[right[i]][right[j]]+m[right[j]][right[i]]
    ans = min(ans, abs(a-b))

def dfs(i, left, right):
    if i==N: cal(left, right)
    if len(left)!=N//2: dfs(i+1, left+[i], right)
    if len(right)!=N//2: dfs(i+1, left, right+[i])
dfs(0,[],[])
print(ans)