from itertools import combinations
def solution(clothes):
    # 딕셔너리로 변환하기
    dic = {}
    for c in clothes:
        v = c[0]
        k = c[1]
        if k not in dic:
            dic[k] = [v]
        else:
            dic[k].append(v)
    k_list = list(dic.keys())
    # 모든 조합찾아서 리스트에 저장
    com = []
    for i in range(1, len(k_list)+1):
        com.append(list(combinations(k_list, i)))
    k_com = sum(com, [])
    # 조합리스트 활용해서 모든 경우의 수 찾기
    all_case = 0
    for kc in k_com:
        case = 1
        for k in kc:
            case *= len(dic[k])
        all_case += case
    answer = all_case

    return answer