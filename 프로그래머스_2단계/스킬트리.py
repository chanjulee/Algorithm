def solution(skill, skill_trees):
    answer = 0
    
    for x in skill_trees: #스킬트리들 배열
        temp = 0
        skillBreak = True
        for y in x: #각 스킬트리 문자열
            if y in skill and y!=skill[temp]:
                skillBreak = False
                break
            if y in skill and y==skill[temp]:
                temp +=1
        if skillBreak == False:
            continue
        answer+=1
    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))