def solution(s):
    count = 0
    removeCount = 0
    while s!='1':
        count+=1
        zeroCount = s.count('0')
        removeCount += zeroCount
        afterRemoveLen = len(s) - zeroCount
        s = bin(afterRemoveLen)[2::]
    return [count, removeCount]
