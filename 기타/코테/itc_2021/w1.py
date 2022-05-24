
'''  
    my = []
    for i, a in enumerate(arr):
        for j, b in enumerate(arr[i+1:]):
            if b < a:
                for c in arr[i+1:][j+1:]:
                    if c < b:
                        my.append([a,b,c])
    
    my = []
    a, b, c = 0, 1, 2
    while 1:
        if arr[a] > arr[b] > arr[c] :
            my.append([arr[a], arr[b], arr[c]])
        if c != len(arr)-1:
            c += 1
        elif b != len(arr)-2:
            b += 1
            c = b+1
        elif a != len(arr)-3:
            a += 1
            b = a+1
            c = b+1
        else:
            break
'''

'''
def sol(arr):
    pivot = 1
    cnt = 0
    while pivot != len(arr)-1 :
        l_cnt , r_cnt = 0, 0
        for l in arr[:pivot]:
            if l > arr[pivot]:
                l_cnt +=1
        for r in arr[pivot+1:]:
            if r < arr[pivot]:
                r_cnt +=1
        cnt += l_cnt*r_cnt
        pivot+=1
    return cnt


arr = [5,3,4,2,1]
print(sol(arr), 7)

arr = [4,1,3,2,5]
print(sol(arr), 1)

arr = [15,10,1,7,8]
print(sol(arr), 3)
'''
'''

'''
'''
from collections import Counter

def substrings(s, k):
    my_cnt = 0
    start = 0
    end = start + k
    while start < len(s):
        temp = 1
        for i in range(10):
            if str(i) in s[start:end] and s[start:end].count(str(i)) != k:
                temp = 0
                break
        my_cnt += temp
        if end < len(s):
            end += k
        else:
            start += 1
            end = start + k
    return my_cnt

print(substrings('1102021222', 2))
print(substrings('1020122', 2))
print(substrings('1221221121', 3))


a = '1010'
print(a[:10])
'''


def solution(m, n, puddles):
    maps = [[0 for _ in range(m+1)] for _ in range(n+1)]
    maps[1][1] = 1
    
    for y in range(1, n+1):
        for x in range(1, m+1):
            if [x, y] == [1, 1]:
                continue
            if [x, y] in puddles:
                continue
            else:
                maps[y][x] = maps[y-1][x] + maps[y][x-1]
                
    return maps[n][m] % 1000000007

def sol(warehouse):
    
    puddles = []
    for x, row in enumerate(warehouse):
        for y, num in enumerate(row):
            if num == 0:
                puddles.append([x, y])

    width = len(warehouse[0])
    height = len(warehouse)
    cnt = 0

    for y in range(1, height+1):
        for x in range(1, width+1):
            if [x, y] == [1, 1]:
                continue
            if [x, y] in puddles:
                continue
            else:
                warehouse[y][x] = warehouse[y-1][x] + warehouse[y][x-1]
                cnt+=1
    
    return cnt



def numPaths(warehouse):
    blocked = []
    n = len(warehouse)
    m = len(warehouse[0])
         
    maps = [[0 for _ in range(m+1)] for _ in range(n+1)]
    if warehouse[0][0] == 1:
        maps[1][1] = 1
    
    for y in range(1, n+1):
        for x in range(1, m+1):
            if [x, y] == [1, 1]:
                continue
            if warehouse[y-1][x-1] == 0:
                continue
            else:
                maps[y][x] = maps[y-1][x] + maps[y][x-1]
                
    return maps[n][m]

warehouse = [ 
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    ]

print(numPaths(warehouse), 10)
    