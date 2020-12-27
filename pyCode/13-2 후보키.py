from itertools import combinations

def solution(relation):
    ck = []
    combi =[]
    column = len(relation[0])
    # 열들의 모든 조합 찾기
    for i in range(1, column):
        combi.extend(combinations(range(column),i))
    # 유일성 검사
    for com in combi:
        col = []
        for i in range(len(relation)):
            col.append(())
            for field in com:
                col[i] = col[i] + (relation[i][field],)
        if len(col) == len(set(col)) :
            ck.append(com)
    
    # 최소성 검사
    for i, c1 in enumerate(ck):
        for c2 in ck[i+1:]:
            c1 = set(c1)
            c2 = set(c2)
            if c1.issubset(c2) :
                c2 = tuple(c2)
                ck.remove(c2)
    answer = len(ck)
    return answer

relation = [
["100","ryan","music","2"],
["200","apeach","math","2"],
["300","tube","computer","3"],
["400","con","computer","4"],
["500","muzi","music","3"],
["600","apeach","music","2"]
]
relation2 = [
['b','2','a','a','b'],
['b','2','7','1','b'],
['1','0','a','a','8'],
['7','5','a','a','9'],
['3','0','a','f','9'],
]
a = solution(relation2)
print(a)


# 시행착오 --------------------------------------
from itertools import combinations

def solution2(relation):
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