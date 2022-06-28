def solution(lottos, win_nums):
    currentRank = getRank(lottos, win_nums)
    zeroCount = lottos.count(0)
    bestRank = currentRank - zeroCount
    if bestRank == 0:
        bestRank = 1
    worstRank = currentRank
    return [bestRank, worstRank]
    
def getRank(lottos, win_nums):
    commonCount = len(list(set(lottos)&set(win_nums)))
    if commonCount == 6:
        return 1
    elif commonCount == 5:
        return 2
    elif commonCount == 4:
        return 3
    elif commonCount == 3:
        return 4
    elif commonCount == 2:
        return 5
    else:
        return 6
    
