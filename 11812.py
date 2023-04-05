import sys
rl = sys.stdin.readline
N, K, Q = map(int ,rl().split())
def caldepth(x):
    if K==1: return x-1
    t, cnt = 1, 0
    while x > t:
        cnt +=1
        t = t+t*K
    return cnt

def findp(x):
    return (x-1)//K

for _ in range(Q):
    a, b = map(int, rl().split())
    ans = 0
    adep, bdep = caldepth(a), caldepth(b)
    if adep < bdep:
        adep, bdep = bdep, adep
        a, b = b, a
    a, b = a-1, b-1
    for _ in range(adep-bdep): a = findp(a)
    ans += adep-bdep
    while True:
        if a==b: break
        ans+=2
        a = findp(a)
        b = findp(b)
    print(ans)