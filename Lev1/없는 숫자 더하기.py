def solution(numbers):
    answer = 0
    for k in range(0,10):
        if k not in numbers:
            answer+=k
    return answer
