n, m  = map(int, input().split())
gh = [list(map(int, input().split())) for _ in range(n)]
dr = [(1,0),(-1,0),(0,1),(0,-1)]
visit = [[0 for _ in range(m)] for _ in range(n)]

def countzero(x, y):
  zero = 0
  if gh[y][x] != 0:
    for dx, dy in dr:
      if gh[y+dy][x+dx] == 0:
        zero += 1
  return zero
cnt = 1
while True:
  dp = [[0 for _ in range(m)] for _ in range(n)]
  for i in range(m):
    for j in range(n):
      dp[j][i] += countzero(i, j)

  for i in range(n):
    for j in range(m):
      gh[i][j] -= dp[i][j]
      if gh[i][j] < 0: gh[i][j] = 0

  visit = [[0 for _ in range(m)] for _ in range(n)]
  ans = 0
  def dfs(x, y):
    global visit
    visit[y][x] = 1
    for dx, dy in dr:
      if visit[y+dy][x+dx] == 0 and gh[y+dy][x+dx] != 0:
        dfs(x+dx, y+dy)

  for i in range(m):
    for j in range(n): 
      if gh[j][i] != 0 and visit[j][i] == 0:
        ans += 1
        dfs(i, j)
  if ans == 0:
    print(0)
    break
  elif ans != 1:
    print(cnt)
    break
  cnt+= 1
  for j in gh:
    print(j)
  print("")