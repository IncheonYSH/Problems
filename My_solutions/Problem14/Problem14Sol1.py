def solution(priorities, location):
    answer = 0    
    while True > 0:
        if priorities[0] == max(priorities):
            answer += 1
            if location == 0:
                break
            location -= 1
            priorities.pop(0)
        else:
            pop_p = priorities.pop(0)
            priorities.append(pop_p)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    return answer