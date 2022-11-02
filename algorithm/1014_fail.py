import sys
N = int(sys.stdin.readline())
dr = [(1,1),(1,0),(-1,0),(-1,1)]

def dfs(x, y):
  if x > 0 or x > col-1 or y < 0 or y > row-1: return
  elif graph[y][x] == 'x': return
  else:
    graph[y][x] = '!'
    for dx, dy in dr:
      try: graph[y+dy][x+dx] = 'x'
      except: continue


for _ in range(N):
  row, col = map(int, sys.stdin.readline().split())
  graph = [list(sys.stdin.readline().rstrip()) for _ in range(row)]
  graph = graph[::-1]
  dp = []
  for i in range(row):
    for j in range(col):
      if graph[i][j] == '.':
        pass

# dp = [n][(m+1)//2][(m+1)//2]