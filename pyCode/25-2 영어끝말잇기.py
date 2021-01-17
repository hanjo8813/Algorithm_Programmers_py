def solution(n, words):
    answer = [0, 0]
    # 단어 리스트를 인덱스와 함께 순회
    for i, w in enumerate(words):
        # 처음 단어는 패스한다.
        if i == 0:
            continue
        # 1. 바로 앞 단어의 끝과 현 단어의 첫 글자가 다르거나
        # 2. 해당 단어가 앞에서 이미 나왔다면?
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
