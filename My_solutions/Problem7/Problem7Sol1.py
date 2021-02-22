import re
def solution(new_id):
    stage_1 = new_id.lower()
    stage_2 = re.sub(r'[^a-z0-9-_.]','',stage_1)
    stage_3 = re.sub(r'\.{2,}','.',stage_2)
    stage_4 = re.sub(r'^\.|\.$','',stage_3)
    
    if len(stage_4) == 0:
        stage_5 = 'a'
    else:
        stage_5 = stage_4
    
    if len(stage_5) >= 16:
        stage_6 = stage_5[:15]
        stage_6 = re.sub(r'\.$','',stage_6)
    else:
        stage_6 = stage_5
       
    while len(stage_6) <= 2:
        stage_6 = stage_6 + stage_6[-1]
    
    stage_7 = stage_6
    
    answer = stage_7
    return answer