def solution(n, words):
    answer = [0, 0]
    for i, w in enumerate(words):
        if i == 0:
            continue
        if (words[i-1][-1:] != w[:1]) or (w in words[:i]):
            answer[0] = i%n + 1
            answer[1] = i//n + 1
            break
    return answer


n = 3 
words = ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']
print(solution(n, words))	

n = 5
words = ['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure', 'establish', 'hang', 'gather', 'refer', 'reference', 'estimate', 'executive']
print(solution(n, words))	

n=2
words = ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']
print(solution(n, words))   # [1,3]
