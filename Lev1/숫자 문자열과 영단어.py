def solution(s):
    stringBucket = []
    answerString = ''
    for k in range(len(s)):
        if s[k].isdigit():
            answerString += s[k]
        else:
            stringBucket += s[k]
        if ''.join(stringBucket) == 'zero':
            answerString += '0'
            stringBucket.clear()
        elif ''.join(stringBucket) == 'one':
            answerString += '1'
            stringBucket.clear()
        elif ''.join(stringBucket) == 'two':
            answerString += '2'
            stringBucket.clear()
        elif ''.join(stringBucket) == 'three':
            answerString += '3'
            stringBucket.clear()
        elif ''.join(stringBucket) == 'four':
            answerString += '4'
            stringBucket.clear()
        elif ''.join(stringBucket) == 'five':
            answerString += '5'
            stringBucket.clear()
        elif ''.join(stringBucket) == 'six':
            answerString += '6'
            stringBucket.clear()
        elif ''.join(stringBucket) == 'seven':
            answerString += '7'
            stringBucket.clear()
        elif ''.join(stringBucket) == 'eight':
            answerString += '8'
            stringBucket.clear()
        elif ''.join(stringBucket) == 'nine':
            answerString += '9'
            stringBucket.clear()
    return int(answerString)
