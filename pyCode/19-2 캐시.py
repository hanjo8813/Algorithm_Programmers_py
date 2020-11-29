from collections import deque
def solution(cacheSize, cities):
    time = 0
    # 싹다 대문자로 만들어놓고 시작
    cities = [c.upper() for c in cities]
    # 빈 큐를 생성
    queue = deque([])
    for c in cities:
        # cache hit
        if c in queue:
            time +=1
            queue.remove(c)
            queue.append(c)
        # cache miss
        else :
            time +=5
            queue.append(c)
            # 아직 큐가 안채워졌을 때
            if len(queue) <= cacheSize:
                continue
            else:
                queue.popleft()
    return time
    
cacheSize = 3
cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 
'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']
print(solution(cacheSize, cities))
