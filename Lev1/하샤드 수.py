def solution(x):
    dividor = 0
    for k in range(len(str(x))):
        dividor += int(str(x)[k])
    if(x % dividor == 0):
        return True
    else:
        return False
