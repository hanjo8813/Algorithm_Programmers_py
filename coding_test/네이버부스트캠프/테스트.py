def solution(v):
    x_set = set()
    y_set = set()
    
    for x, y in v:
        x_set.add(x)
        y_set.add(y)
    
    v_list = []
    for x in x_set:
        for y in y_set:
            v_list.append([x,y])
    
    for vertex in v_list:
        if vertex not in v:
            return vertex

v = [[1, 4], [3, 4], [3, 10]]
print(solution(v))