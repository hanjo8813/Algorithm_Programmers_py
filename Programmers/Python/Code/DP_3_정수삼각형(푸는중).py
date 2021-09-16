def travel(triangle, i, j, order, order_sum):
    if i == len(triangle):
        value_list = order_sum.values()
        return max(value_list)
    next_order = order + str(j)
    order_sum[next_order] = order_sum[order] + triangle[i][j]
    a = travel(triangle, i+1, j, next_order, order_sum)
    b = travel(triangle, i+1, j+1, next_order, order_sum)
    return max(a, b)

def solution(triangle):
    order_sum = {"" : 0}
    answer = travel(triangle, 0, 0, "", order_sum)
    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
a = solution(triangle)
print(a)

# 효율성통과안됨. 오답임. 다시풀어야됨.