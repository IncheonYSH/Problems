from decimal import *
def solution(lines):
    def binary_search(sorted_list, target):
        right = len(sorted_list) - 1
        left = 0
        if sorted_list[-1] <= target:
            return right
        while True:
            mid = (left + right) // 2
            if sorted_list[mid] <= target and target < sorted_list[mid + 1]:
                break
            elif sorted_list[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return mid
    
    log_length = len(lines)
    lines_end = [0] * log_length
    lines_start = [0] * log_length
    T = [0] * log_length
    for i, ele in enumerate(lines):
        end = int(ele[11:13]) * 3600 * 1000\
            + int(ele[14:16]) * 60 * 1000\
            + int(ele[17:19]) * 1000\
            + int(ele[20:23])
        t = int(Decimal(ele[24:-1]) * 1000)
        start = end - t + 1
        lines_end[i] = end
        T[i] = t
        lines_start[i] = start
    lines_start_sorted = sorted(lines_start)
    
    max_dps = 0
    for i, ele in enumerate(lines_end):
        if log_length - i <= max_dps:
            break
        count_left = i
        target_right = ele + 999
        target_right_index = binary_search(lines_start_sorted, target_right)
        count_right = log_length - target_right_index - 1
        count_dps = log_length - count_left - count_right
        if count_dps > max_dps:
            max_dps = count_dps
        else:
            continue
    
    answer = max_dps        
    return answer