def solution(a, b):
    answer = 0
    if(a<=b):
        for k in range(a,b+1):
            answer+=k
    elif(b<a):
        for k in range(b,a+1):
            answer+=k
    return answer
