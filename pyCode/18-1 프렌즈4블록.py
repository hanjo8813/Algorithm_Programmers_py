import copy   
def modify(m, n, board):
    b_copy = copy.deepcopy(board)  
    for i in range(m):
        sign = False
        for j in range(n):
            if b_copy[i][j] == "_":
                continue
            if j==n-1 or b_copy[i][j] != b_copy[i][j+1]:
                if sign==True:
                    sign = False
                else:
                    b_copy[i][j]="_"                
            else:
                sign = True
    for j in range(n):
        sign = False
        for i in range(m):
            if b_copy[i][j] == "_":
                continue
            if i==m-1 or b_copy[i][j] != b_copy[i+1][j]:
                if sign==True:
                    sign = False
                else:
                    b_copy[i][j]="_"                
            else:
                sign = True
    for i in range(m):
        for j in range(n):
            if b_copy[i][j] != "_" and b_copy[i][j-1]=="_" and b_copy[i][j+1]=="_":
                b_copy[i][j]="_"
    for j in range(n):
        for i in range(m):
            if b_copy[i][j] != "_" and b_copy[i-1][j]=="_" and b_copy[i+1][j]=="_":
                b_copy[i][j]="_"

    # 모든 검사 했는데 뺄 대상이 없다면?
    if sum(b_copy, []).count("_") == m*n:
        return sum(board, []).count("_")

    index = [[] for _ in range(n)]
    for i in range(m):
        for j in range(n):
            if b_copy[i][j] == "_":
                index[j].append((i,j))
            else:
                b_copy[i][j] = "_"
    for j in range(n):
        index[j].sort(reverse=True)
        for i in range(m-1, -1, -1):
            if not index[j]:
                break
            else:
                row = index[j][0][0]
                col = index[j][0][1]
                index[j].remove(index[j][0])
                b_copy[i][j] = board[row][col]
    return modify(m, n, b_copy)
    
def solution(m, n, board):
    # 리스트로 변환하기
    for i, b in enumerate(board):
        board[i] = list(b)
    answer = modify(m, n, board)
    return answer

m = 4
n = 5
board = ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']
m2 = 6	
n2 = 6	
board2 = [
    'TTTANT', 
    'RRFACC', 
    'RRRFCC', 
    'TRRRAA', 
    'TTMMMF', 
    'TMMTTJ']

print(solution(m2, n2, board2))