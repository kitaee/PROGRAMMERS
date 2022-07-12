def solution(s):
    openCount = 0
    closeCount = 0

    for string in s:
        if string == '(':
            openCount+=1
        else:
            closeCount+=1
        if openCount<closeCount:
            return False
    if openCount!=closeCount:
        return False
    return True
