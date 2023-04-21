import sys
rl = sys.stdin.readline
N = int(rl())
MAXV = 1000000
tree = [0 for _ in range(MAXV*4)]

def update(left, right, node, x, w):
    if x<left or x>right: return
    if left==right: tree[node] += w
    else:
        mid = (left+right)//2
        update(left, mid, node*2, x, w)
        update(mid+1, right, node*2+1, x, w)
        tree[node] = tree[node*2]+tree[node*2+1]

def caltree(left, right, node, s, e):
    if e<left or s>right: return 0
    if s<=left and right<=e: return tree[node]
    mid = (left+right)//2
    return caltree(left,mid,node*2,s,e)+caltree(mid+1,right,node*2+1,s,e)

def cal(idx):
    def divCon(left, right):
        if left>=right: return left
        mid = (left+right)//2
        if caltree(0,MAXV,1,1,mid)>=idx: return divCon(left, mid)
        else: return divCon(mid+1, right)
    out = divCon(0,MAXV)
    update(0,MAXV,1,out,-1)
    return out

for _ in range(N):
    a, *b = map(int, rl().split())
    if a==1: print(cal(b[0]))
    else: update(0,MAXV,1,b[0],b[1])