def solution(n):
    n = bin(n)
    answer = n[2:].count('1')
    return answer

n = 5000
print(solution(n))