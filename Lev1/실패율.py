def solution(N, stages):
    answer = []
    failure = {}
    stagesLen = len(stages)
    
    for k in range(1, N+1):
        if stagesLen==0:
            failure[k] = 0
        else:
            challenger = stages.count(k)
            failure[k] = challenger/stagesLen
            stagesLen-=challenger
        
    sortedFailure = sorted(failure.items(), key = lambda x : x[1], reverse = True)
    
    for key, value in sortedFailure:
        answer.append(key)
    return answer
