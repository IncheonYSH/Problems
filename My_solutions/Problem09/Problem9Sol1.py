def solution(skill, skill_trees):
    skill_length = len(skill)
    number_trees = len(skill_trees)
    det = [True] * number_trees
    for i in range(number_trees):
        det_in = []
        for j in range(skill_length):
            if skill_trees[i].find(skill[j]) == -1:
                det_in.append(27)
            else:
                det_in.append(skill_trees[i].find(skill[j]))
        det[i] = det_in
        det[i] = all(det[i][k] <= det[i][k + 1] for k in range(len(det[i]) - 1))
    answer = sum(det)
    return answer