from math import gcd
def solution(w,h):
    g = gcd(w, h)
    gw = w / g
    gh = h / g
    answer = w*h - g*(gh + gw -1)
    return answer

a = solution(8,12)
print(a)