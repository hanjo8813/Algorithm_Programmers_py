# 테케 반만맞음
# 효율성은 하나도 통과못함 ㅠ

from collections import deque

def solution(n, k, cmd):
    li = [i for i in range(n)]
    cache = deque([])

    for c in cmd:
        # 커서 이동 관련
        if c[0] == 'D':
            k += int(c[2])
            while k >= len(li):
                k -= len(li)
        elif c[0] == 'U':
            k -= int(c[2])
            while k < 0:
                k += len(li)
        # 데이터 삭제/되돌리기
        elif c[0] == 'C':
            # 삭제후 cache에 저장 [인덱스 , 값(최초인덱스)]
            cache.appendleft([k, li.pop(k)])
            # 삭제후 커서가 맨 뒤일 경우
            if k == len(li):  
                k-=1
        elif c[0] == 'Z':
            idx, v = cache.popleft()
            if k >= idx :
                k+=1
            li.insert(idx, v)

    answer = ['O' for _ in range(n)]
    for idx, v in cache:
        answer[v] = 'X'
    answer = ''.join(answer)
        
    return answer
    


cmd1 = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(8,2,cmd1), "OOOOXOOO")

cmd2 = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(8,2,cmd2), "OOXOXOOO")