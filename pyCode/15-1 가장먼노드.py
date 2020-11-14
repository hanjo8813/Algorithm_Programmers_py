from collections import deque
def solution(n, edge):
    # 정점의 인접 정점 리스트
    # a_vertex = [[3, 2], [3, 1, 4, 5], [6, 4, 2, 1], [3, 2], [2], [3]]
    a_vertex =[[] for _ in range(n)]
    for v1, v2 in edge:
        a_vertex[v1-1].append(v2)
        a_vertex[v2-1].append(v1)
    # 정점 1로부터의 거리와 방문여부를 저장하는 딕셔너리
    dic_dis = {1:0}
    # 방문할 순서를 저장하는 큐
    queue = deque([1])
    # 그래프 순회(BFS)
    # 1. 큐에서 정점을 꺼내고 그 정점의 인접 정점을 방문
    # 2. 첫 방문시 그 정점을 딕셔너리에 저장 + 큐에다가 추가
    # 3. 만약 딕셔너리 key값이 이미 존재하면 재방문임.
    while queue:
        q = queue.popleft()
        for v in a_vertex[q-1]:
            if v not in dic_dis.keys():
                dic_dis[v]=dic_dis[q]+1
                queue.append(v)
    # 이렇게 저장된 딕셔너리의 값(거리)중 가장 큰값 찾기
    dv = list(dic_dis.values())
    answer = dv.count(max(dv))
    return answer

n = 6
edge = [[3, 6], [4, 3], [3, 2], 
[1, 3], [1, 2], [2, 4], [5, 2]]
a = solution(n, edge)
print(a)