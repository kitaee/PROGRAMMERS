def solution(n, lost, reserve):
    realLost = list(set(lost) - set(reserve))
    realReserve = list(set(reserve) - set(lost))
    realLost.sort()
    realReserve.sort()
    lostCount = len(realLost)
    for lostStudent in realLost:
        if lostStudent-1 in realReserve:
            lostCount-=1
            realReserve.remove(lostStudent-1)
        elif lostStudent+1 in realReserve:
            lostCount-=1
            realReserve.remove(lostStudent+1)
    return n-lostCount
