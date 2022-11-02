import sys

def cal(a, b):
  out = 32
  visit = [[1 for _ in range(m)] for _ in range(n)]
  for i in range(n):
    for j in range(m):
      if graph[i][j] == a and (i+j)%2==0:
        visit[i][j] = 0
      elif graph[i][j] == b and (i+j)%2==1:
        visit[i][j] = 0
  for i in range(n-8+1):
    for j in range(m-8+1):
      ans = 0
      for t in range(8):
        ans += sum(visit[i+t][j:j+8])
      out = min(out, ans)
  return out

n, m = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
print(min(cal("W", "B"), cal("B", "W")))
