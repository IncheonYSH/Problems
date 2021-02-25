import re
def solution(n):
    answer = ''
    digit = None
    pattern_1 = ['1', '2', '4'] 
    pattern_2 = ['4', '1', '2'] 
    def to_digit(x, pattern):
        if x % 3 == 1:
                digit = pattern[0]
        elif x % 3 == 2:
            digit = pattern[1]
        elif x % 3 == 0:
            digit = pattern[2]
        return digit
    
    while True:
        if n // 3 == 0:
            answer = to_digit(n, pattern_1) + answer
            break
        digit = to_digit(n, pattern_1)
        n = n // 3
        if digit == '4':
            if n <= 3:
                n = n - 1
                if n % 3 != 0:
                    answer = to_digit(n, pattern_1) + digit + answer
                    break
                else:
                    answer = digit + answer
                    break
            else:
                n = n - 1
                answer = digit + answer
        else:
            if n<= 3:
                answer = to_digit(n, pattern_1) + digit + answer
                break
            else:
                answer = digit + answer
        
    return answer