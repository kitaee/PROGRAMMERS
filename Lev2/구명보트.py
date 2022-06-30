def solution(people, limit):
    answer = 0
    startIndex = 0
    endIndex = len(people)-1
    people.sort()
    
    while(startIndex<endIndex):
        if people[startIndex] + people[endIndex] <= limit:
            startIndex+=1
            endIndex-=1
        else:
            endIndex-=1
        answer+=1
    if startIndex>endIndex:
        return answer
    else:
        return answer+1
