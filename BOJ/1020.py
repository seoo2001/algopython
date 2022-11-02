c = [6, 2, 5, 5, 4, 5, 6, 3, 7, 5] # 2, 3, 4, 7: 1 / 5: 4 / 6: 2
n = input()
nsum = 0
for x in n: nsum += c[int(x)]
dp = [[10**len(n)]*(7*len(n)+1) for _ in range(len(n)+1)]
for j in range(2, 8):
  dp[1][j] = c.index(j)
for i in range(2, len(n)+1):
  for j in range(2*i, 7*i+1):
    for t in range(2, j+1):
      dp[i][j] = min(dp[i][j], int(str(dp[1][t])+str(dp[i-1][j-t])))
check, breaker = False, False
if c[int(n[-1])] in c[int(n[-1])+1:]:
  for i, x in enumerate(c):
    if x == c[int(n[-1])] and i > int(n[-1]):
      t = str(i)
      break
  print(int(n[:len(n)-1]+t)-int(n))
  check = True
else:
  for i in range(2, len(n)+1):
    if breaker == True: break
    k = []
    t = sum(c[int(x)] for x in n[-i:])
    for j in range(10):
      if 2*(i-1) <= t-c[j] <= 7*(i-1):
        if int(str(j)+str(dp[i-1][t - c[j]]).zfill(i-1)) > int(n[-i:]):
          print(int(n[:len(n)-i]+str(j)+str(dp[i-1][t - c[j]]).zfill(i-1))-int(n))
          breaker = True
          break
if not breaker and not check:
  print(10**len(n) + dp[len(n)][nsum] - int(n))