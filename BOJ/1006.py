import sys
N = int(sys.stdin.readline())

def sol(x, y):
    for i in range(nodeNum-1):
        if solList[0][i] + solList[0][i+1] <= solNum: dp[i+1][1] = dp[i][2] + 1
        else: dp[i+1][1] = dp[i][0] + 1
        if solList[1][i] + solList[1][i+1] <=solNum: dp[i+1][2] = dp[i][1] + 1
        else: dp[i+1][2] = dp[i][0] + 1
        if solList[0][i+1] + solList[1][i+1] <= solNum: dp[i+1][0] = dp[i][0] + 1
        else: dp[i+1][0] = min(dp[i+1][1], dp[i+1][2]) + 1
        if solList[0][i] + solList[0][i+1] <= solNum and solList[1][i] + solList[1][i+1] <=solNum:
            dp[i+1][0] = min(dp[i-1][0] + 2, dp[i+1][0])
    return dp[x][y]

for _ in range(N):
    nodeNum, solNum = map(int, sys.stdin.readline().split())
    solList = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]

    # 0: ALL, 1: 1~N, 2: N+1~2N return dp[7][0]
    dp = [[0 for _ in range(3)] for _ in range(nodeNum)]
    
    # case 1: 순환부에 연결이 없을 때
    dp[0][1], dp[0][2] = 1, 1
    if solList[0][0] + solList[1][0] <= solNum: dp[0][0] = 1
    else: dp[0][0] = 2
    answer = sol(nodeNum-1, 0)
    #case 2: 순환부에 연결
    dp = [[0 for _ in range(3)] for _ in range(nodeNum)]    
    if solList[0][0] + solList[0][-1] <= solNum:
        temp = solList[0][0]
        solList[0][0] = solNum
        dp[0][1] = 1
        dp[0][2] = 1
        dp[0][0] = 2
        answer = min(answer, sol(nodeNum-1, 2))
        solList[0][0] = temp

    dp = [[0 for _ in range(3)] for _ in range(nodeNum)]
    if solList[1][0] + solList[1][-1] <= solNum:
        temp = solList[1][0]
        solList[1][0] = solNum
        dp[0][1] = 1
        dp[0][2] = 1
        dp[0][0] = 2
        answer = min(answer, sol(nodeNum-1, 1))
        solList[1][0] = temp

    dp = [[0 for _ in range(3)] for _ in range(nodeNum)]
    if solList[0][0] + solList[0][-1] <= solNum and solList[1][0] + solList[1][-1] <= solNum:
        temp = solList[1][0]
        solList[1][0] = solNum
        temp2 = solList[0][0]
        solList[0][0] = solNum
        dp[0][1] = 1
        dp[0][2] = 1
        dp[0][0] = 2
        answer = min(answer, sol(nodeNum-2, 0))
        solList[1][0] = temp
        solList[0][0] = temp2

    
    if nodeNum == 1:
        if solList[0][0] + solList[1][0] <= solNum:
            print(1)
        else: print(2)
    
    else: print(answer)