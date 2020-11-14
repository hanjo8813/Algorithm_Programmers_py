def isBalance(u):
    cnt=0
    for x in u:
        if x=="(" :
            cnt+=1
        else:
            cnt-=1
    if cnt == 0:
        return True
    else :
        return False

def isCorrect(w):
    cnt=0
    for x in w:
        if x=="(" :
            cnt+=1
        else:
            cnt-=1
        if(cnt < 0):
            return False 
    if cnt == 0:
        return True

def split_uv(w):
    if w == "":
        return ""
    u = ""
    v = ""
    for i, x in enumerate(w):
        u = u+x
        if isBalance(u):
            v = w[i+1:]
            break
    if isCorrect(u):
        v = split_uv(v)
        return u+v
    else:
        r = "(" + split_uv(v) + ")"
        u = list(u[1:-1])
        for i, x in enumerate(u):
            if x == "(":
                u[i] = ")"
            else:
                u[i] = "("
        u = ''.join(u)
        return r + u

def solution(p):
    answer = split_uv(p)
    return answer

p = "(()())()"
p1 = ")("
p2 = "()))((()"
p3 = ")()()()()()("

print(p)