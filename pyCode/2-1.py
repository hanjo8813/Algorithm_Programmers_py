def solution(phone_book):
    answer = False
    for i in phone_book:
        length = len(i)
        for j in phone_book:
            if i==j or len(j) <= length:
                continue
            sliced = j[0:length]
            if sliced == i:
                return answer
    answer = True
    return answer