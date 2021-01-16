# 파일명 정렬

### https://programmers.co.kr/learn/courses/30/lessons/17687

<hr>

## 문제 풀이

<br>

> ### 아이디어
1. 초기 값은 0으로 초기화 하고 끝말잇기가 틀린 경우 바꿔줍니다.
2. 단어 리스트를 순회할 때 바로 앞 인덱스의 단어를 불러와야 합니다.
3. 따라서 인덱스와 같이 순회해야하므로 enumerate 함수를 사용합니다.
4. 단어 리스트의 두 번째 값부터 순회합니다.
5. 앞 단어의 끝과 검사할 단어의 첫번째를 슬라이싱을 통해 비교합니다.
6. 또는 현재 단어 앞 까지 슬라이싱한 리스트에 현재 단어가 있다면 answer값을 바꿔줍니다.
7. n은 사람 수이므로 n을 이용한 몫과 나머지 연산을 통해 answer를 구합니다.

<br>

> ### 정답 코드
```python
def solution(n, words):
    answer = [0, 0]
    for i, w in enumerate(words):
        if i == 0:
            continue
        if (words[i-1][-1:] != w[:1]) or (w in words[:i]):
            answer[0] = i%n + 1
            answer[1] = i//n + 1
            break
    return answer
```

<br>

> ### 코드 설명
<h4><a href="../pyCode/25-2 영어끝말잇기.py">이곳을 누르면 설명이 추가된 코드로 이동합니다.</a></h4>
