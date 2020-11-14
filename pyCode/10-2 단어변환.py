end_depth = []

def match(begin, word):
    dif=0
    L_begin = list(begin)
    L_words = list(word)
    for i in range(len(L_words)):
        if L_words[i] != L_begin[i]:
            dif += 1
    if dif == 1:
        return True
    else:
        return False

def DFS(begin, target, words, depth):
    global end_depth
    temp_words = words.copy()
    for i in range(len(words)):
        if match(begin, words[i]):
            if words[i] == target:
                end_depth.append(depth)
                return
            temp_words[i] =""
            DFS(words[i], target, temp_words, depth+1)

def solution(begin, target, words):
    answer = 0
    sign = False

    for i in range(len(words)):
        if words[i] == target:
            sign = True

    if sign == False:
        return answer
    
    DFS(begin, target, words, 1)
    answer = min(end_depth)
    return answer

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
a = solution(begin, target, words)
print(a)