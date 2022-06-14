def solution(n):
    answer = ''
    for k in range(0,n):
        if k%2==0:
            answer += "수"
        else:
            answer += "박"
    return answer
