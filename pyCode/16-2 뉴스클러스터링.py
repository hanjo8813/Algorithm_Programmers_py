def to_piece(str_):
    # 문자열 대문자 -> 소문자
    str_ = str_.lower()
    piece = []
    for i in range(len(str_)-1):
        # 문자열을 두개씩 자른다.
        new_p = str_[i:i+2]
        # 특수문자가 포함된건 거른다.
        if new_p.isalpha() :
            piece.append(new_p)
    return piece

def solution(str1, str2):
    piece1 = to_piece(str1)
    piece2 = to_piece(str2)
    union = 0
    i_s = 0
    # 1과 2의 중복을 제거한 합집합 원소를 순회
    # 1과 2에서의 각 원소당 등장횟수를 구한다.
    # 합집합에는 등장횟수의 max값을, 교집합에는 min값을 더한다.
    for s in set(piece1) | set(piece2):
        union += max(piece1.count(s), piece2.count(s))
        i_s += min(piece1.count(s), piece2.count(s))
    # 자카드 유사도 계산
    # 교집합과 합집합이 둘다 공집합인 경우엔 유사도 = 1
    if i_s == 0 and union == 0:
        J = 1
    else :
        J = i_s / union
    answer = int(J * 65536)
    return answer

a = solution('FRANCE','french')
b = solution('handshake','shake hands')
c = solution('aa1+aa2','AAAA12')
d = solution('E=M*C^2','e=m*c^2')

print(a, 16384)
print(b, 65536)
print(c, 43690)
print(d, 65536)
