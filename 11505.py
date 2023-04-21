import sys
rl = sys.stdin.readline
D=1000000007
N,M,K=map(int, rl().split())
ns = [int(rl()) for _ in range(N)]
tree = [0 for _ in range(4*N)]
def init(left, right, node):
    if left==right:
        tree[node] = ns[left]
        return tree[node]
    mid = (left+right)//2
    tree[node] = (init(left, mid, node*2)*init(mid+1, right, node*2+1))%D
    return tree[node]
init(0,N-1,1)

def update(left, right, node, x, w):
    if x<left or x>right: return
    if left == right: tree[node] = w
    else:
        mid = (left+right)//2
        update(left,mid,node*2,x,w)
        update(mid+1,right,node*2+1,x,w)
        tree[node] = (tree[2*node]*tree[2*node+1])%D

def cal(left, right, node, s, e):
    if right<s or left>e: return 1
    if s<=left and right<=e: return tree[node]
    mid = (left+right)//2
    return (cal(left,mid,node*2,s,e)*cal(mid+1,right,node*2+1,s,e))%D

for _ in range(M+K):
    a,b,c= map(int, rl().split())
    if a==1: update(0,N-1,1,b-1,c)
    else: print(cal(0,N-1,1,b-1,c-1)%D)