def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    commonStudent = []
    lostCount = len(lost)
    for lostStudent in lost:
        if lostStudent in reserve:
            commonStudent.append(lostStudent)
    for lostStudent in lost:
        if lostStudent in commonStudent:
            reserve.remove(lostStudent)
            lostCount-=1
            continue
        if lostStudent-1 in reserve:
            reserve.remove(lostStudent-1)
            lostCount-=1
            continue
        if lostStudent+1 in reserve and lostStudent+1 not in commonStudent:
            reserve.remove(lostStudent+1)
            lostCount-=1
    answer = n-lostCount
    return answer
