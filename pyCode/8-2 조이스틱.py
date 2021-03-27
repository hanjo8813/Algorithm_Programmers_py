import string 
def solution(name):
    al = string.ascii_uppercase
    # 효율적인 좌우 이동거리 추출
    l_name = len(name)
    start, end = 0, 0
    lr = []
    while True:
        if l_name > end+1 and name[end+1] == 'A': 
            end += 1
        else:
            lr.append((start*2-1) + (l_name-end))
            if l_name != end+1:
                start = end+1
                end = start
            else:
                break
    # 알파벳 상하 최소 이동 추출
    ud = 0
    for n in name:
        n_idx = al.index(n)
        if n_idx > 13:
            n_idx = 26 - n_idx
        ud += n_idx
    return ud + min(lr)

print(solution("JAZ") , 11)
print(solution("JEROEN") , 56)
print(solution("JAN") , 23)
print(solution("BBBAAAB"), 9)
print(solution("ABABAAAAABA"), 11) #11
print(solution("AAA"), 0)







# 10 11 통과 안됨
def solution2(name):
    al = string.ascii_uppercase
    len_name = len(name)
    complete = [0] * len_name
    cursor = 0
    count = len_name -1
    direction = 1
    while len_name != sum(complete):
        # 좌우 커서 움직임 조절
        if name[cursor] == 'A'and cursor <= len_name/2 and direction==1:
            complete[cursor] = 1
            count -=1
            cursor = -1
            direction = -1
        # 상하 알파벳 조절
        loc_al = al.index(name[cursor])
        if loc_al > 13:
            loc_al = 26 - loc_al
        count += loc_al
        # 완료 표시 후 커서 이동
        complete[cursor] = 1
        cursor += direction
        print(complete)
        print(count)
    return count





