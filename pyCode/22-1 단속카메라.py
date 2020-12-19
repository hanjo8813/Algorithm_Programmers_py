def solution(routes):
    routes = sorted(routes, key= lambda x : (x[0]))
    print(routes)
    ex_left = routes[0][0]
    ex_right = routes[0][1]
    camera =  0
    for L, R in routes:
        if ex_left <= L:
            ex_left = L
            if ex_right >= R:
                camera +=1
            if 


    print(routes)
    return 


routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3], [20,30]]
print(solution(routes))