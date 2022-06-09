def solution(arr1, arr2):
    answer=[]
    for i in range(len(arr1)):
        tempList = []
        for k in range(len(arr1[i])):
            tempList.append(arr1[i][k] + arr2[i][k])
        answer.append(tempList)
    return answer
