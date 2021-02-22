def solution(number, k):
    number = str(number)
    number_length = len(number)
    remain_length = number_length - k
    number_list = [int(number[i]) for i in range(number_length)]
    answer = ''
    start_index = -1
    target_number = 1
    while remain_length > 0:
        # target_number = max(number_list[start_index + 1:number_length + (-1)*remain_length + 1])
        target_number = 0
        for i in range(start_index + 1, number_length + (-1)*remain_length + 1):
            if target_number == 9:
                target_number = 9
                break
            elif target_number < number_list[i]:
                target_number = number_list[i]
            else:
                continue
        answer = answer + str(target_number)        
        start_index = number_list.index(target_number, start_index + 1, number_length)
        remain_length -= 1
    return answer