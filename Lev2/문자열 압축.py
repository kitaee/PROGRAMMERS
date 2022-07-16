def solution(s):
    if len(s)==1:
        return 1
    minimunLen = 9999
    for i in range(1, len(s)//2+1):
        index = 0
        newString = ''
        count = 1
        while index < len(s):
            if s[index : index+i] == s[index+i : index + 2*i]:
                count+=1
            else:
                if count==1:
                    newString+=s[index : index+i]
                else:
                    newString+=str(count)
                    newString+=s[index : index+i]
                    count=1
            index = index + i
        if len(newString) < minimunLen:
            minimunLen = len(newString)
    return minimunLen
        
    
