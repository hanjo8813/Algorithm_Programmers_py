def solution(array, commands):
    answer = []
    for c in commands:
        i = c[0]-1
        j = c[1]
        k = c[2]-1
        if i==j:
            answer.append(array[i])
            continue
        piece = array[i : j]
        piece.sort()
        answer.append(piece[k])
    return answer