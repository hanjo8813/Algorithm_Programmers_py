cnt = 0

def loop(i, people, limit):
    global cnt
    if people[i]+people[i+1] <= limit:
        cnt +=1
        if i+2 == len(people)-1:    # i+2가 마지막 인덱스라면 인덱스가 하나만 남는다는 뜻이므로 검사할 필요없이 cnt+1
            cnt+=1
            return
        elif i+2 > len(people)-1:   # i+2가 마지막 인덱스보다 크다면 더이상 뒤에 인덱스가 없음. 그냥 리턴
            return
        loop(i+2, people, limit)
        
    else:
        cnt +=1
        if i+1 == len(people)-1:    # i+1이 마지막 인덱스라면 인덱스가 하나만 남는다는 뜻이므로 검사할 필요없이 cnt+1
            cnt +=1
            return
        loop(i+1, people, limit)

def solution(people, limit):
    people.sort()
    loop(0, people, limit)
    return cnt