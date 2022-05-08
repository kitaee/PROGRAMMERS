def solution(n):
    answer = 0
    for k in range(len(str(n))):
        answer+=int(str(n)[k])
    return answer
