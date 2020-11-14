def solution(clothes):
    # 딕셔너리로 변환하기
    dic = {}
    for c in clothes:
        if c[1] not in dic:
            dic[c[1]] = 1
        else:
            dic[c[1]] += 1
    case = 1
    for v in dic.values() :
        case = case * (v+1)
    answer = case-1
    return answer

# 2 1 >> 5
clothes1 = [
    ['yellow_hat', 'headgear'], 
    ['blue_sunglasses', 'eyewear'], 
    ['green_turban', 'headgear']]
# 3 >> 3
clothes2 = [
    ['crow_mask', 'face'], 
    ['blue_sunglasses', 'face'], 
    ['smoky_makeup', 'face']]
# 1 1 1 > 7
clothes3 = [
    ['crow_mask', 'face'], 
    ['blue_sunglasses', 'eyewear'], 
    ['yellow_hat', 'headgear']]

print(solution(clothes3))