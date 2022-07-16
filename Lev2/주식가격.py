def solution(prices):
    answer = []
    for i in range(len(prices)):
        if prices[i] == 1:
            answer.append(len(prices)-i-1)
            continue
        if i==len(prices)-1:
            answer.append(0)
            break
        count=1
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                answer.append(count)
                break
            else:
                if j==len(prices)-1:
                    answer.append(count)
                    break
                count+=1
    return answer
