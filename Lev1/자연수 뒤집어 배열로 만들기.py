def solution(n):
    answer = []
    n=str(n)
    for k in range(len(n)):
        answer.append(int(n[k]))
    answer = list(reversed(answer))
    return answer
