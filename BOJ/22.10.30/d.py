import sys
rl = sys.stdin.readline
fl = sys.stdout.flush

n = int(input())
x = 2
while True:
  print("? "+str(x))
  fl()
  t = int(rl())
  if t == x//2:
    print("! "+str(x))
    break
  else: x = t*2
