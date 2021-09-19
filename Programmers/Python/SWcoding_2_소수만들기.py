from itertools import combinations
# 소수인지 판별하는 함수
def isPrime(n):
    # 1과 자기 자신으로 나누어지지 않는게 소수.
    # 1과 자기 자신을 제외한 값들로 모두 나눠본다
    for i in range(2, n):
        if n%i==0:
            return False
    return True

def solution(nums):
    # 리스트의 모든 조합 찾기
    combi = list(combinations(nums,3))
    # 경우의 수를 찾는 것이므로 중복된 소수가 나와도 +1이다.
    answer = 0
    for c in combi:
        s = sum(c)
        if isPrime(s):
            answer+=1
    return answer

nums = [1,2,7,6,4]
print(solution(nums))