def solution(array, commands):
    answer=[]
    slicedArr=[]
    for command in commands:
        slicedArr=array[command[0]-1:command[1]]
        slicedArr.sort()
        answer.append(slicedArr[command[2]-1])
    return answer
