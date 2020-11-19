
<h1><strong ><a href="https://programmers.co.kr/learn/courses/30/lessons/43164">여행경로</a></strong></h1>
<hr>

## 문제설명
주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 ICN 공항에서 출발합니다.

항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

## 제한사항
- 모든 공항은 알파벳 대문자 3글자로 이루어집니다.
- 주어진 공항 수는 3개 이상 10,000개 이하입니다.
- tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 - 항공권이 있다는 의미입니다.
- 주어진 항공권은 모두 사용해야 합니다.
- 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 - 경로를 return 합니다.
- 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.

## 입출력 예

|tickets|	return|
|---|---|
|[[ICN, JFK], [HND, IAD], [JFK, HND]]|	[ICN, JFK, HND, IAD]|
|[[ICN, SFO], [ICN, ATL], [SFO, ATL], [ATL, ICN], [ATL,SFO]] | 	[ICN, ATL, ICN, SFO, ATL, SFO]|

## 입출력 예 설명
예제 #1

`[ICN, JFK, HND, IAD]` 순으로 방문할 수 있습니다.

예제 #2

`[ICN, SFO, ATL, ICN, ATL, SFO]` 순으로 방문할 수도 있지만 `[ICN, ATL, ICN, SFO, ATL, SFO]` 가 알파벳 순으로 앞섭니다.

<hr>

## 문제 풀이

> ### 아이디어
1. 공항을 정점으로 보고 티켓의 정보를 방향간선으로 본다면 방향그래프를 구현할 수 있다.
2. 방향그래프의 모든 정점을 순회하고 그 경로를 저장해야하기 때문에 깊이우선탐색(DFS)를 이용해 모든 정점을 순회한다.
3. tickets는 방향 간선이기때문에 tickets를 읽으면 인접 정점을 알 수 있다. (인접리스트와 유사)
4. 다음 정점을 방문하려면 tickets의 티켓들을 쓴다고 생각한다.
5. 그리고 방문하는 정점들을 모두 route에 기록하고, 티켓을 모두 다 쓴다면 기록된 경로를 전역리스트 route_list에 저장한다.
6. 모든 탐색이 끝나면 route_list에서 알파벳순위가 높은 경로를 추출한다.

<br>

> ### 정답 코드
```python
route_list = []
def DFS(vertex, tickets, route):
    r_copy = route.copy()
    r_copy.append(vertex)
    if not tickets:
        global route_list
        route_list.append(r_copy)
        return
    for t in tickets:
        if t[0] == vertex:
            t_copy = tickets.copy()
            t_copy.remove(t)
            DFS(t[1], t_copy, r_copy)
            
def solution(tickets):
    DFS("ICN", tickets, [])
    global route_list
    route_list.sort()
    answer = route_list[0]
    return answer
```

> ### 코드 설명
<h4><a href="../pyCode/17-1 여행경로.py">이곳을 누르면 설명이 추가된 코드로 이동합니다.</a></h4>
