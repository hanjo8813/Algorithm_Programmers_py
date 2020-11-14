from itertools import permutations

def solution(numbers):
    str_per_list=[]
    per = list(permutations(numbers, len(numbers)))
    for p in per:
        str_per = "".join([str(_) for _ in p])
        str_per_list.append(int(str_per))
    answer = max(str_per_list)
    return answer

# 효율성 초과됨. -> 다시풀어야됨