n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
g2 = list(map(list, zip(*graph)))
def checkline(ln):
    i = 1
    while i < n:
        if ln[i] == ln[i-1] or ln[i] == ln[i-1]-0.5: i+=1
        elif ln[i]-1 == ln[i-1]:
            for j in range(l):
                if i-1-j < 0: return False
                if ln[i-1-j] != ln[i]-1: return False
            i+=1
        elif ln[i]+1 == ln[i-1] or ln[i] + 1.5 == ln[i-1]:
            for j in range(l):
                if i+j >= n: return False
                if ln[i+j] == ln[i-1]-1 or ln[i+j] == ln[i-1]-1.5: ln[i+j] += 0.5
                else: return False
            i+=l
        else: return False
    return True
ans = 0
for i in graph:
    if checkline(i): ans += 1
for i in g2:
    if checkline(i): ans += 1
print(ans)