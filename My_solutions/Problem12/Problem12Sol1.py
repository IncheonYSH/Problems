import re

def solution(s):
    action_count = 0
    zero_count = 0
    while s != "1":
        length_before = len(s)
        s = re.sub(r'0','',s)
        length_after = len(s)
        diff = length_before - length_after
        zero_count += diff
        s = bin(len(s))[2:]
        action_count += 1
    answer = [action_count, zero_count]
    return answer