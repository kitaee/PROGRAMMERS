def solution(numbers, target):
    answerList = [numbers[0], -numbers[0]]
    for k in range(1, len(numbers)):
        tempList = []
        for i in range(len(answerList)):
            tempList.append(answerList[i] + numbers[k])
            tempList.append(answerList[i] - numbers[k])
        answerList = tempList
    return answerList.count(target)
