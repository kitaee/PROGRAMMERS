def solution(board):
    answer = 0
    n = len(board)
    m = len(board[0])
    dp = []
    
    for i in range(n):
        tempDp = []
        for j in range(m):
            tempDp.append(0)
        dp.append(tempDp)
    
    dp[0] = board[0]
    for k in range(1, n):
        dp[k][0] = board[k][0]
    
    for i in range(1,n):
        for j in range(1,m):
            if board[i][j] == 0 :
                dp[i][j] = 0
                continue
            dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1
    
    for k in range(len(dp)):
        tempMax = max(dp[k])
        answer = max(tempMax, answer)
    return answer**2
    
