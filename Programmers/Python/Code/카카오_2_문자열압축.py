# def solution(s):
#     q, r = divmod(len(s), 2)
#     if r : q -= 1

#     result_list = []
#     for n in range(1, q+1):
#         cur = 0
#         result_str = ''
#         print(n)
#         while cur < len(s):
#             cur_str = s[cur:cur + n]
#             count = 1
#             for i in range(cur + n, len(s)+1, n):
#                 next_str = s[i:i+n]
#                 if cur_str == next_str:
#                     count +=1
#                 else:
#                     if count == 1 :
#                         result_str += s[cur]
#                         cur +=1
#                     else:
#                         result_str += str(count) + cur_str
#                         cur = i
#                     break
#         print(result_str)
#         result_list.append(result_str)
#     print(result_list)
#     answer = 0
#     return answer


# def solution(s):
#     # q, r = divmod(len(s), 2)
#     # if r : q -= 1
#     count_list = []
#     for n in range(1, len(s)//2):
#         before_str = s[0:n]
#         flag = False
#         count = n
#         if before_str == s[n:2*n]:
#             flag = True
#             count = 0
        
#         for i in range(n, len(s), n):
#             cur_str = s[i:i+n]
#             print(before_str, cur_str)
#             if before_str == cur_str:
#                 flag = True
#             else:
#                 if flag:
#                     count += n+1
#                 else:
#                     count += len(before_str)
#                 before_str = cur_str
#                 flag = False
#             print(n, count)
#             print()
#         if flag:
#             count += n+1
#         else:
#             count += len(before_str)
#         count_list.append(count)
#     print(count_list)
#     return


def solution(s):
    length_list = []
    if len(s):
        return 1
    for n in range(1, len(s)//2+1):
        count = 1
        result_str = ''
        for i in range(0, len(s), n): 
            cur_str = s[i:i+n]
            next_str = s[i+n:i+n+n]
            if cur_str == next_str:
                count += 1
            else:
                if count != 1:
                    result_str += str(count) + cur_str
                else:
                    result_str += cur_str
                count = 1
        length_list.append(len(result_str))
    return min(length_list)


s = "aabbaccc"
print(solution(s), 7)

s = "ababcdcdababcdcd"
print(solution(s), 9)

s = "abcabcdede"
print(solution(s), 8)

s = "abcabcabcabcdededededede"
print(solution(s), 14)

s = "xababcdcdababcdcd"
print(solution(s), 17)

s = "xxxxxxxxxxyyy"
print(solution(s), 5)

s="a"
print(solution(s), 5)

