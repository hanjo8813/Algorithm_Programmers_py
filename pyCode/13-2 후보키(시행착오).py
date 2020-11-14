from itertools import combinations

def solution(relation):
    new_rel = []
    for row in relation:
        dic = {}
        for index, col in enumerate(row):
            dic[index] = col
        new_rel.append(dic)

    combi = []
    for row in new_rel:
        for i in range(1, len(new_rel)):
            for com in combinations(row.items(), i):
                combi.append(com)

    #중복제거
    same = []
    for index, i in enumerate(combi):
        for j in combi[index+1:]:
            if i==j :
                same.append(i)
    same = set(same)
    same = list(same)

    item = []
    c_combi =[]
    for i in range(len(relation[0])):
        item.append(i)
    for i in range(1,len(item)):
        c_combi.append(list(combinations(item, i)))
    c_combi = sum(c_combi, [])

    for s1 in same:
        index = ()
        for s2 in s1:
            index = index + (s2[0],)
        if index in c_combi:
            c_combi.remove(index)
    
    for i, c1 in enumerate(c_combi):
        for c2 in c_combi[i+1:]:
            sc1 = "".join([str(_) for _ in c1])
            sc2 = "".join([str(_) for _ in c2])
            if sc1 in sc2:
                c_combi.remove(c2)
    answer = len(c_combi)
    return answer