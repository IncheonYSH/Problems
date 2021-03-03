import re
def solution(p):
    def is_balance(s):
        if s.count('(') == s.count(')'):
            det = True
        else:
            det = False
        return det
        
    def is_pair(s):
        while len(s) > 0:
            length_before = len(s)
            s = re.sub(r'\(\)', '', s)
            length_after = len(s)
            if length_before == length_after:
                break
        if len(s) == 0:
            det = True
        else:
            det = False
        return det
    
    def process(s):
        if len(s) == 0:
            return s
        else:
            for k in range(1, len(s) + 1):
                if is_balance(s[0:k]) == False:
                    continue
                else:
                    u = s[0:k]
                    v = s[k:]
                    break

            if is_pair(u) == True:
                u = u + process(v)
                return u

            else:
                cache = '(' + process(v) + ')'
                u = u[1:-1]
                mapping = u.maketrans("()",")(")
                u = u.translate(mapping)
                cache = cache + u
                return cache
            
    if is_pair(p) == True:
        answer = p
    else:
        answer = process(p)
    return answer