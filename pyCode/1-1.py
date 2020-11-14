def solution(participant, completion):
    
    participant.sort()
    completion.sort()
    
    for i in range(len(participant)):
        if i == len(participant)-1:
            answer = participant[i]
            return answer
        elif participant[i] != completion[i]:
            answer = participant[i]
            return answer
             

# 정렬 후 part배열의 길이만큼 포문을 돌린다. 
# 만약 i가 part배열의 마지막 인덱스까지 왔다면 마지막으로 남은 이름이므로 그게 답. 
# 그게 아니라면 part와 comp배열을 서로 비교해 다른 값이 나오게 된다면 
# comp에는 없는 이름이므로 part배열값이 답.