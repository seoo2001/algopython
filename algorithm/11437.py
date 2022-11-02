import sys
rl = sys.stdin.readline
n = int(rl())
gh = [[] for _ in range(n+1)]
for _ in range(n-1):
  v, w = map(int, rl().split())
  gh[v].append(w)
  gh[w].append(v)
qn = int(rl())
qt = [list(map(int, rl().split())) for _ in range(qn)]
q = [1]
parentnode = [0 for _ in range(n+1)]
parentnode[1] = -1
while q:
  node = q.pop()
  for x in gh[node]:
    if parentnode[x] == 0:
      parentnode[x] = node
      q.append(x)

for x, y in qt:
  xq, yq = [x], [y]
  while x!= -1:
    x = parentnode[x]
    xq.append(x)
  while y!= -1:
    y = parentnode[y]
    yq.append(y)
  for i in range(1, n):
    try:
      if xq[-i] != yq[-i]:
        print(xq[-i+1])
        break
    except:
      if len(xq) < len(yq):
        print(xq[0])
      else: print(yq[0])
      break
# print(parentnode)
# print(gh)