def solution(prices):
    length = len(prices)
    uptime = [0] * length
    for i in range(length):
        for j in range(i + 1, length):
            if prices[i] > prices[j]:
                uptime[i] = j - i
                break
            elif j == length - 1:
                uptime[i] = length - i - 1
            else:
                continue
    answer = uptime
    return answer