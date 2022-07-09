def solution(priorities, location):
    answer = 0
    while True:
        if priorities[0] == max(priorities):
            if location == 0:
                answer+=1
                break
            else:
                answer+=1
                priorities.pop(0)
                location-=1
        else:
            priorities.append(priorities.pop(0))
            location-=1
        if location == -1:
            location = len(priorities)-1
    return answer
