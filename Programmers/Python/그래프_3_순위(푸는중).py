from collections import deque
count = [0]
def DFS(i, a_list, is_visit, depth):
    depth+=1
    check=0
    # 방문표시
    iv_copy = is_visit.copy()
    iv_copy[i]=0

    for next_v in a_list[i]:
        # 인접 정점이 첫방문일 경우만 방문.
        if iv_copy[next_v]==1:
            DFS(next_v, a_list, iv_copy, depth)
            check+=1
    # 인접 정점을 다 검사 후
    # 만약 모든 정점들이 방문 되었다면? -> 해당 깊이를 저장
    if sum(iv_copy) == 0 or sum(iv_copy)-check==0:
        global count
        count.append(depth)
        return

def solution(n, results):
    # 방향그래프의 정점당 인접리스트 생성
    a_list = [[] for _ in range(n)]
    for a, b in results:
        a_list[b-1].append(a-1)
    print(a_list)
    # 방문 여부 저장
    is_visit = [1 for _ in range(n)]
    # DFS
    for i in range(n):
        DFS(i, a_list, is_visit, 0)
    global count
    return max(count)


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [1, 4]]
print(solution(n, results))

n = 5
results = [[3, 5], [4, 2], [4, 5], [5, 1], [5, 2]]
print(solution(n, results))


# 잘못이해하고 푼 솔루션......
def solution2(n, results):
    # 2차원 배열 평탄화 -> 중복제거 -> 정점 개수 구하기
    num_v = len(set(sum(results, [])))
    # 방향그래프의 정점당 인접리스트 생성
    a_list = [[] for _ in range(num_v)]
    for a, b in results:
        a_list[b-1].append(a)
    # 방문여부 저장하기, n부터 방문이므로 방문체크
    isvisit = [0 for _ in range(num_v)]
    isvisit[n-1] = 1
    # 방문할 큐 생성, n부터 방문
    queue = deque([n])

    # BFS
    while queue :
        q = queue.popleft()
        for next_v in a_list[q-1]:
            # 인접 정점이 아직 방문안했을 때
            if isvisit[next_v-1]==0:
                isvisit[next_v-1]=1
                queue.append(next_v)
    rank = sum(isvisit)

    return rank



def solution3(n, results):
    # 방향그래프의 정점당 진출/진입 간선
    out_list = [[] for _ in range(n)]
    in_list = [[] for _ in range(n)]
    for a, b in results:
        out_list[b-1].append(a-1)
        in_list[a-1].append(b-1)
  
    print(out_list)
    print(in_list)

    return 