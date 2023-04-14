import sys
rl = sys.stdin.readline
w, n = map(int, rl().split())
l = list(map(int, rl().split()))
dp = [0]*799995
l.sort()
flag = False
for i in range(2,n):
    for j in range(0,i-1): dp[l[j]+l[i-1]] = 1
    for j in range(i+1, n):
        if l[i]+l[j] > w: break
        if dp[w-l[i]-l[j]]: flag = True
    
    if flag: break
print("YES" if flag else "NO")

