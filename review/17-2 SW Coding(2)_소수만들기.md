
<h1><strong ><a href="https://programmers.co.kr/learn/courses/30/lessons/12977">소수만들기</a></strong></h1>
<hr>

## 문제설명
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

## 제한사항
- nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
- nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.

## 입출력 예

|nums|	result|
|---|---|
|[1,2,3,4]|	1|
|[1,2,7,6,4]|	4|

## 입출력 예 설명
입출력 예 #1   
[1,2,4]를 이용해서 7을 만들 수 있습니다.

입출력 예 #2   
[1,2,4]를 이용해서 7을 만들 수 있습니다.   
[1,4,6]을 이용해서 11을 만들 수 있습니다.   
[2,4,7]을 이용해서 13을 만들 수 있습니다.   
[4,6,7]을 이용해서 17을 만들 수 있습니다.

<hr>

## 문제 풀이

> ### 아이디어
1. 입력된 숫자 리스트의 3가지 원소를 가진 모든 조합을 구한다.
2. 그리고 그 조합을 모두 더한 값이 소수인지 아닌지 판별한다.
3. 소수일때 경우의 수를 +1 해주면 총 경우의 수가 나온다.

<br>

> ### 알게 된 함수/방법
- `combinations` : itertools 라이브러리의 내장함수. `combination(조합구할리스트, 원소 수)`로 조합을 구해준다. 다만 반환형이 리스트가 아니므로 리스트로 변환해줘야함.

<br>

> ### 정답 코드
```python
from itertools import combinations
def isPrime(n):
    for i in range(2, n):
        if n%i==0:
            return False
    return True

def solution(nums):
    combi = list(combinations(nums,3))
    answer = 0
    for c in combi:
        s = sum(c)
        if isPrime(s):
            answer+=1
    return answer
```

> ### 코드 설명
<h4><a href="../pyCode/17-2 소수만들기.py">이곳을 누르면 설명이 추가된 코드로 이동합니다.</a></h4>
