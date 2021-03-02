import copy
def solution(n):
#     [1, 1] = 1
#     [2, 1] = 2
#     [3, 1] = 4
#     ...
#     [n, 1] = n * (n - 1) / 2 + 1
#     [n, 2] = n * (n - 1) / 2 + 2
#     ...
#     [n, m] = n * (n - 1) / 2 + m
#   
#     일반식
#     [n, m] = n * (n - 1) / 2 + m    

    def list_index(n, m):
        return int(n * (n - 1) / 2 + m)      
    
    num_triangle = (n - 1) // 3 + 1
    end_number = int(n * (1 + n) / 2)
    index = [0] * end_number
    answer = index.copy()
    loop_start = 1
    for j in range(num_triangle):
        n_corrected = n - 3 * j
        margin_col = j
        margin_row = 2 * j
        if n_corrected == 1:
            loop_end = loop_start + 1
        else:
            loop_end = loop_start + 3 * (n_corrected - 1)
            
        for i in range(loop_start, loop_end): # triangle
            i_corrected = i - (loop_start - 1)
            if i_corrected <= n_corrected:
                index[i - 1] = list_index(i_corrected + margin_row, 1 + margin_col) - 1
            elif i_corrected <= 2 * n_corrected - 1:
                index[i - 1] = list_index(n_corrected + margin_row,
                                          i_corrected - (n_corrected - 1) + margin_col) - 1
            else:
                index[i - 1] = list_index(3 * n_corrected - i_corrected - 1 + margin_row,
                                          3 * n_corrected - i_corrected - 1 + margin_col) - 1
        loop_start = loop_end
    for i in range(end_number):
         answer[index[i]] = i + 1
    return answer