import sys
rl = sys.stdin.readline
gene = rl().rstrip()
n = int(rl())
dic = {}
for _ in range(n):
  v, w = map(str, rl().split())
  if w in dic: dic[w].append(v)
  else: dic[w] = [v]

def findminlen(s, word):
  w = 0
  for i in range(s, len(gene)):
    if word[w] == gene[i]:
      w += 1
      if w == 3: return i
  return -1

dp = [[len(gene) for _ in range(len(dic))] for _ in range(len(gene))]
for s in range(len(gene)):
  for i, (key, elems) in enumerate(dic.items()):
    for elem in elems:
      dis = findminlen(s, elem)
      if dis != -1:
        dp[s][i] = min(dp[s][i], dis)
dp2 = [0 for _ in range(len(gene)+1)]
for i in range(len(dic)):
  if dp2[dp[0][i]] < len(gene): dp2[dp[0][i]] += 1

check = [[0 for _ in range(len(dic))] for _ in range(len(gene))]
for j in range(3, len(gene)):
  for i in range(j-2, -1, -1):
    for t in range(len(dic)):
      if dp[i][t] == j:
        for x in range(0, i):
          if check[x][t] == 0 and dp2[x] != 0:
            dp2[j] += dp2[x]
            check[x][t] = 1
print(sum(dp2[:len(dp2)-1])%1000000007)