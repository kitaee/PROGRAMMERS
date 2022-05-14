def solution(arr):
    answer=[]
    answer.append(arr[0])
    for k in range(1,len(arr)):
        if(answer[-1]==arr[k]):
            continue
        else:
            answer.append(arr[k])
    return answer
        
