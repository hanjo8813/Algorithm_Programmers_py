def solution(prices):
    answer = []
    for i in range(len(prices)):
        answer.append(0)
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i]+=1
            else:
                answer[i]+=1
                break
    return answer
            
prices = [1, 2, 3, 2, 3]
prices2 = [3, 2, 1, 2, 1]
prices3 = [5,4,3,2,1]
prices4 = [1,2,3,2,3,3,1]
print(solution(prices4))