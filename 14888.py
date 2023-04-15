import sys
rl = sys.stdin.readline
N = int(rl())
ns = list(map(int, rl().split()))
caln = list(map(int, rl().split()))
amax, amin = -1e9, 1e9
def cal(out, i, a, b, c, d):
    global amax, amin
    if i == N: amax = max(amax, out); amin = min(amin, out)
    if a: cal(out+ns[i],i+1,a-1,b,c,d)
    if b: cal(out-ns[i],i+1,a,b-1,c,d)
    if c: cal(out*ns[i],i+1,a,b,c-1,d)
    if d:
        if out < 0: cal(-(-out//ns[i]),i+1,a,b,c,d-1) 
        else: cal(out//ns[i],i+1,a,b,c,d-1)

cal(ns[0], 1, caln[0],caln[1],caln[2],caln[3])
print(amax, amin, sep="\n")