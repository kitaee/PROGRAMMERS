def solution(n, arr1, arr2):
    answer = []
    for k in range(len(arr1)):
        num1 = bin(arr1[k])[2::].zfill(n)
        num2 = bin(arr2[k])[2::].zfill(n)
        printString = ''
        for i in range(0,n):
            if num1[i]=='1' or num2[i]=='1':
                printString += '#'
            else:
                printString += ' '
        answer.append(printString)
    return answer
    
