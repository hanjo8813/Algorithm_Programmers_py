from collections import deque
def solution(n, edge):
    dic_v = {}
    for i in range(1, n+1):
        dic_v[i] = []
        for e in edge:
            if i in e:
                dic_v[i].append(e)
    dic_dis = {1:0}
    queue = deque([1])

    while queue:
        q = queue.popleft()
        dis = dic_dis[q]
        vertex = dic_v[q]
        for v in vertex:
            #print(q, v, dic_dis)
            next_v = None
            if v[0] == q:
                next_v = v[1]
            elif v[1] == q:
                next_v = v[0]
            if next_v != None and (next_v not in dic_dis.keys()):
                dic_v[next_v].remove(v)
                dic_dis[next_v]=dis+1
                queue.append(next_v)

    dv = list(dic_dis.values())
    answer = dv.count(max(dv))
    return answer