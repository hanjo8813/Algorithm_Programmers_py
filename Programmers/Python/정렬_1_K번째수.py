def solution2(array, commands):
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

def solution(array, commands):
    answer = []
    for a, b, c in commands:
        answer.append(sorted(array[a-1:b])[c-1])
    return answer


array = [1, 5, 2, 6, 3, 7, 4]	
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))


