import sys

N = int(sys.stdin.readline())
for _ in range(N):
    pos = list(map(float, sys.stdin.readline().split()))
    pointNum = int(sys.stdin.readline())
    pointPos = [list(map(float, sys.stdin.readline().split())) for _ in range(pointNum)]
    answer = 0
    for x, y, r in pointPos:
        a = (x-pos[0])**2 + (y-pos[1])**2 < r**2
        b = (x-pos[2])**2 + (y-pos[3])**2 < r**2
        if (not a and b) or (a and not b): answer += 1
    print(answer)