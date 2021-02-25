def solution(progresses, speeds):
    answer = []
    length = len(progresses)
    remain = [0] * length
    for i in range(length):
        d, h = divmod(100 - progresses[i], speeds[i])
        if h != 0:
            d += 1
        remain[i] = d
    remain.append(101)
    n = remain[0]
    count = 0
    for j in remain:
        if j > n:
            answer.append(count)
            n = j
            count = 1
        else:
            count += 1
    return answer