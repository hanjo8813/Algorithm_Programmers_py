def solution(files):
    s_files = []
    for f in files:
        # head
        for j in range(len(f)):
            # 처음으로 숫자가 등장할 경우
            if f[j].isdigit():
                # 첫 숫자 등장한 인덱스를 저장
                start = j
                break
        # number
        for k in range(start, start+5):
            end = k+1
            # 만약 문자열의 끝까지 갔다면 인덱스 저장
            if k == len(f)-1:
                break
            # number 영역에서 첫 문자가 등장햇을 때 인덱스를 저장
            if f[k].isdigit()==0:
                end-=1
                break

        # 위에서 저장된 인덱스대로 슬라이싱 후 리스트에 저장
        # 원본 -> index 0
        # head는 대소문자 구별 안하므로 소문자로 변환 -> index 1
        # number는 숫자 크기로 비교해야하므로 int형으로 변환 (앞의 0도 제거) -> index 2
        s_files.append([f, f[:j].lower(), int(f[start:end])])

    # 정렬 기준 1번은 head, 2번은 number.
    s_files = sorted(s_files, key = lambda x : (x[1], x[2]))
    answer=[]
    for f in s_files:
        answer.append(f[0])
    return answer


    

files = ['img000012345', 'img1.png','img2', 'IMG02', 'abc123defg123.jpg']
print(solution(files))
files = ['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG']
print(solution(files))
files = ['foo010bar020.zip']
print(solution(files))
files = ['img000002345645']
print(solution(files))
