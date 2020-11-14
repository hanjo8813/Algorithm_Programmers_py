end_dic = {1:0}

def DFS(start, depth, edge):
    global end_dic
    temp_edge = edge.copy()
    for e in edge:
        if e[0] == start:
            temp_edge.remove(e)
            if e[1] not in end_dic:
                end_dic[e[1]] = depth
            elif end_dic[e[1]] > depth:
                end_dic[e[1]] = depth
            DFS(e[1], depth+1, temp_edge)
        elif e[1] == start:
            temp_edge.remove(e)
            if e[0] not in end_dic:
                end_dic[e[0]] = depth
            elif end_dic[e[0]] > depth:
                end_dic[e[0]] = depth
            DFS(e[0], depth+1, temp_edge)

def solution(n, edge):
    DFS(1, 1, edge)
    global end_dic
    max_depth = max(end_dic.values())
    answer = 0
    for v in end_dic.values():
        if v == max_depth :
            answer+=1
    return answer

n = 6
edge = [[3, 6], [4, 3], [3, 2], 
[1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))