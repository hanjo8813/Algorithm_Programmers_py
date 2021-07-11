from collections import Counter

def solution(arr):
    count = list(Counter(arr).values())
    count = [n for n in count if n != 1]
    if not count:
        return -1
    else:
        return count
    

arr = [3,2,4,4,2,5,2,5,5]
print(solution(arr))
arr = [3,5,7,9,1]
print(solution(arr))
