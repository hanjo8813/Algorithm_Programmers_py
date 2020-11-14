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
