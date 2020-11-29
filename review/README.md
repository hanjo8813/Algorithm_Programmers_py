# <파이썬 문법 정리>

## 문자열 관련 
- `replace(기존값, 바꿀값)` :
- `strip(삭제할값, )` : 
- `split(나눌 기준)`

---

## 리스트 관련
- `append(값)` : 리스트 맨 뒤에 해당 값 그 자체를 추가한다. 1개만 추가됨
- `extend(값)` : 리스트 맨 뒤에 가장 바깥쪽 iterable의 모든 값을 추가한다. (한 단계를 풀어서 넣는다고 생각)
- `remove(값)` : 리스트를 뒤져서 해당 값을 하나만 삭제 (맨 앞에거)
- `pop(인덱스)` : 해당 인덱스에 해당하는 값을 삭제 후 반환
- `index(값)` : 찾는 값에 해당하는 인덱스를 반환
- `sort(list, key, reverse)` : 해당 리스트를 정렬
- `sorted(list, key, reverse)` : 해당 리스트를 정렬하고 반환
- `sum(리스트)` : 리스트에 있는 값 모두 더한 값 반환

---

## 집합 관련

---

## 튜플 관련

---

## 딕셔너리 관련

---

## 기타 함수

- `enumerate(zip(리스트))` : zip으로 두 리스트를 묶고 순회하면 튜플로 출력, 그 튜플에 인덱스까지 추출하기
- `sum(2차원리스트, [])` : 2차원리스트 입력시 모두 flatten해서 1차원리스트로 반환.

---

## 외부 함수
> ### from collections import deque
> - `deque` : 컬렉션의 내장함수. 리스트를 큐의 형태로 바꿀때 사용한다.
>    - `popleft()` : 큐에서 가장 왼쪽 값 pop
>    - `append, remove, extend` : 기존 리스트와 동일

> ### from collections import Counter
> - `Conter(리스트)` : 입력된 리스트의 원소들의 등장횟수를 구해서 원소별 등장횟수 딕셔너리를 반환해준다. ex) {a : 5}

> ### from collections import defaultdict
>- `= defaultdict(기본값)` : 입력값에 자료형이나 람다 함수를 넣어 기본값을 정의할 수 있는 딕셔너리.

> ### from itertools import combinations/permutations
- `combinations(대상리스트, 원소 수)` : 입력된 원소 수에 해당하는 조합을 구해준다. 다만 반환형이 리스트가 아니므로 리스트로 변환해줘야함.
- `permutations(대상리스트, 원소 수)` : 입력된 원소 수에 해당하는 순열을 구해준다.

> ### from operator import itemgetter
- `itemgetter(_)` : sorted함수 안에서 key의 값으로 사용됨. 2차원 리스트일 경우 원소 리스트의 열을 기준으로 정렬된다. (key에 lambda x:x[_] 를 넣은것과 동일) ex) key=itemgetter(1)

> ### import copy
- `copy.deepcopy(복사할 리스트)` : 2차원 리스트는 기존의 .copy()함수로 복사가 되지 않는다. 따라서 2차원 리스트르 복사하려면 왼쪽의 형식에 복사하고싶은 리스트를 입력하면 복사된 리스트가 반환된다.





