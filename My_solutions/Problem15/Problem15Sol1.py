import re
import copy
def solution(phone_book):
    phone_book = sorted(phone_book)
    answer = True
    det = {'z':1}
    for i in phone_book:
        det_loop = det.copy()
        for j in det_loop.keys():
            pattern_1 = '^' + j + '[0-9]+'
            m_1 = re.compile(pattern_1)
            if m_1.match(i):
                return False
            else:
                det[i] = 1
    return answer