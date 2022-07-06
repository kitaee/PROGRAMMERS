from collections import deque

def solution(begin, target, words):
    answer = 0
    visited = [False]*len(words)
    if target not in words:
        return answer

    queue = deque()
    queue.append([begin,0])
    while queue:
        myWord, count = queue.popleft()
        if myWord == target:
            answer = count
            break
        for k in range(len(words)):
            if wordCheck(myWord, words[k]) == 1 and visited[k] == False:
                queue.append([words[k], count+1])
                visited[k] = True
    return answer
    
def wordCheck(myWord, targetWord):
    count = 0
    for k in range(len(myWord)):
        if myWord[k] != targetWord[k]:
            count+=1
    return count
