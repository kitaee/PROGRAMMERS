def solution(citations):
    citations.sort()
    for k in range(0, citations[-1]+1):
        count=0
        for citation in citations:
            if k<=citation:
                count+=1
        if k>count:
            return k-1
    return 0
