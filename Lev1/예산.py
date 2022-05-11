def solution(d, budget):
    answer=0
    d = sorted(d)
    for k in range(len(d)):
        budget -= d[k]
        answer+=1
        if(budget<0):
            answer-=1
            break
    return answer
