def solution(board, moves):
    answer = 0
    bucket = []
    for move in moves:
        index = 0
        while board[index][move-1] == 0:
            index+=1
            if index == len(board):
                break
        if index != len(board):                
            bucket.append(board[index][move-1])
            if len(bucket)>1:
                if bucket[-1]==bucket[-2]:
                    bucket.pop()
                    bucket.pop()
                    answer+=2
            board[index][move-1] = 0
    return answer
