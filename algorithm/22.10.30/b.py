case = [float(input()) for _ in range(10)]
ans = 1
case.sort()
for i in range(1, 10):
  ans = ans * case[i] / i
print(ans*1e9)