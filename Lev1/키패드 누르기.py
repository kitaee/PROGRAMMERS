keypad = {1: [0,0], 2: [0,1], 3: [0,2], 4: [1,0], 5: [1,1], 6: [1,2],
         7: [2,0], 8: [2,1], 9: [2,2], '*': [3,0], 0: [3,1], '#': [3,2]}

def solution(numbers, hand):
    answer = ''
    leftPosition=['*']
    rightPosition=['#']
    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            answer+='L'
            leftPosition.append(number)
        elif number == 3 or number == 6 or number == 9:
            answer+='R'
            rightPosition.append(number)
        else:
            answer+=distanceChecking(leftPosition[-1],rightPosition[-1],number,hand)
            if answer[-1] == 'L':
                leftPosition.append(number)
            else:
                rightPosition.append(number)
    return answer
    
def distanceChecking(left,right,target,hand):
    leftDistance = abs(keypad[target][0]-keypad[left][0]) + abs(keypad[target][1]-keypad[left][1])
    rightDistance = abs(keypad[target][0]-keypad[right][0]) + abs(keypad[target][1]-keypad[right][1])
    if leftDistance < rightDistance:
        return 'L'
    elif leftDistance > rightDistance:
        return 'R'
    else:
        if hand == 'left':
            return 'L'
        else:
            return 'R'
