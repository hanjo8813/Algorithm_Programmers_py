# heapq나 deque 사용시 보다 수행시간 20배나 느림;;
def solution(jobs):
    jobs.sort()
    time_now, take_time_list = 0, []
    while jobs:
        # 요청시점이 현재시간을 넘는 값이 처음 등장할 때를 찾는다
        for i, job in enumerate(jobs):
            if job[0] > time_now:
                break
            else:
                i+=1
        # i를 기점으로 리스트를 슬라이싱하여 따로 정렬한 후 다시 합친다.
        # 현 시간보다 작을 때는 작업시간 기준, 클 때는 둘 다 기준.
        jobs = sorted(jobs[:i], key=lambda x:x[1]) + sorted(jobs[i:], key=lambda x:(x[0],x[1]))
        request,run = jobs.pop(0)
        # 요청시점이 현 시간보다 클때는 현 시점을 바꿔야 한다.
        if request > time_now:
            time_now = request
        time_now += run
        # 요청시간~끝난 시간을 구해서 리스트에 저장.
        take_time_list.append(time_now - request)
    # 소요 시간의 평균 구하기
    answer = sum(take_time_list)//len(take_time_list)
    return answer




jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))
'''
print(solution([[0, 10], [2, 10], [9, 10], [15, 2]]), 14)
print(solution([[0, 10], [2, 12], [9, 19], [15, 17]]), 25)
print(solution([[0, 3], [1, 9], [2, 6]]), 9)
print(solution([[0, 1]]), 1)
print(solution([[1000, 1000]]), 1000)
print(solution([[0, 1], [0, 1], [0, 1]]), 2)
print(solution([[0, 1], [0, 1], [0, 1], [0, 1]]), 2)
print(solution([[0, 1], [1000, 1000]]), 500)
print(solution([[100, 100], [1000, 1000]]), 550)
print(solution([[10, 10], [30, 10], [50, 2], [51, 2]]), 6)
print(solution([[0, 3], [1, 9], [2, 6] , [30, 3]]), 7)
print(solution([[0, 3], [1, 9], [2, 6]]), 9)
print(solution([[0, 10], [4, 10], [5, 11], [15, 2]]), 15)
print(solution([[0, 3], [1, 9], [2, 6], [4, 3]]), 9)
print(solution([[0, 1], [1, 2], [500, 6]]), 3)
print(solution([[0, 3], [1, 9], [500, 6]]), 6)
print(solution([[0, 1], [0, 1], [1, 0]]), 1)
print(solution([[0, 3], [4, 3], [8, 3]]), 3)
print(solution([[0, 3], [4, 3], [10, 3]]), 3)
print(solution([[0, 5], [6, 2], [6, 1]]), 3)
print(solution([[0, 5], [6, 1], [6, 2]]), 3)
print(solution([[0, 5], [2, 2], [5, 3]]), 5)
print(solution([[0, 5], [2, 2], [4, 2]]), 5)
print(solution([[0, 3], [0, 1], [4, 7]]), 4)
print(solution([[0, 2], [3, 6], [3, 1]]), 3)
print(solution([[0, 5], [1, 2], [5, 5]]), 6)
print(solution([[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]), 13)
print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]), 72)
print(solution([[1, 9], [1, 4], [1, 5], [1, 7], [1, 3]]), 13)
'''


# 개삽질
def try_solution(jobs):
    time_now = jobs.pop(0)[1]
    take_time_list = [time_now]
    while jobs:
        for i, job in enumerate(jobs):
            if job[0] > time_now:
                break
            i+=1
        a,b = sorted(jobs[:i], key=lambda x:x[1]).pop(0)
        take_time_list.append(time_now - a + b)
        time_now += b
        jobs.remove([a,b])
    
    answer = sum(take_time_list)//len(take_time_list)
    return answer