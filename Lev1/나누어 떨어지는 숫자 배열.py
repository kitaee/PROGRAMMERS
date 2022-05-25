def solution(arr, divisor):
    answer = []
    for k in range(len(arr)):
        if(arr[k] % divisor == 0):
            answer.append(arr[k])
    answer = sorted(answer)
    if(len(answer)==0):
        answer.append(-1)
    return answer
