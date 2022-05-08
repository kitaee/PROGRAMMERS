def solution(n):
    for k in range(2,n):
        if(n%k==1):
            return k
