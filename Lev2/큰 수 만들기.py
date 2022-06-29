def solution(number, k):
    answerLen = len(number)-k
    stack=[number[0]]
    for i in range(1,len(number)):
        while stack[-1] < number[i] and k>0:
            stack.pop()
            k-=1
            if len(stack)==0:
                break
        stack.append(number[i])
    return ''.join(stack)
