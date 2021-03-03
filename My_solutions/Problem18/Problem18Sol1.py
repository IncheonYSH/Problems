import copy
def solution(arr1, arr2):
    nrows = len(arr1)
    ncols = len(arr2[0])
    answer = []
    for i in range(nrows):
        answer.append([])
        for j in range(ncols):
            arr22 = [arr2[k][j] for k in range(len(arr2))]
            answer[i].append(sum([x * y for x, y in zip(arr1[i], arr22)]))
    return answer