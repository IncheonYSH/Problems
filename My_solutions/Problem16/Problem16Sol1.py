import re
import copy
def solution(s):
    answer = len(s)
    max_n = answer // 2

    for n in range(1, max_n + 1):
        compressed = ''
        s_copy = s
        while len(s_copy) >0:
            pattern = '^(' + s_copy[0:n] + '){2,}'
            r = re.compile(pattern)
            m = r.match(s_copy)
            if m:
                split_index = m.span()[1]
                count = split_index // n
                compressed = compressed + str(count) + s_copy[0:n]
                s_copy = re.sub(pattern, '', s_copy)
            else:
                compressed = compressed + s_copy[0:n]
                s_copy = s_copy[n:]
        if len(compressed) < answer:
            answer = len(compressed)
    return answer