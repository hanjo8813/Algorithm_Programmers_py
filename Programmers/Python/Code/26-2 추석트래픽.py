from datetime import datetime, timedelta

def solution(lines):
    # 문자열을 시간 데이터로 파싱
    log_list = []
    for l in lines:
        a, b, c = l.split(' ')
        end = datetime.strptime(a+' '+b, '%Y-%m-%d %H:%M:%S.%f')
        sec = float(c.replace('s', ''))
        start = end - timedelta(seconds = sec - 0.001)
        log_list.append([start, end])

    cnt_list = []
    for start, end in log_list:
        # 타임아웃이 3초까지이므로 +3 까지 검사한다
        for t in range(4):
            # 검사 구간 설정
            section_start = start + timedelta(seconds = t)
            section_end = section_start + timedelta(seconds = 0.999)
            # 만약 검사 시작 구간이 해당 로그의 끝보다 클 때
            if section_start > end:
                section_start = end
                section_end = end + timedelta(seconds = 0.999)
            cnt = 0
            for log_start, log_end in log_list:
                # 검사 구간을 양쪽으로 완전히 벗어난 로그는 제외
                if not (log_end < section_start or section_end < log_start):
                    cnt += 1
            cnt_list.append(cnt)
    # 검사한 구간들에서의 cnt 최대값만 리턴
    return max(cnt_list)



lines = [
'2016-09-15 01:00:04.002 2.0s',
'2016-09-15 01:00:07.000 2s'
]
print(solution(lines))


lines = [
'2016-09-15 20:59:57.421 0.351s',
'2016-09-15 20:59:58.233 1.181s',
'2016-09-15 20:59:58.299 0.8s',
'2016-09-15 20:59:58.688 1.041s',
'2016-09-15 20:59:59.591 1.412s',
'2016-09-15 21:00:00.464 1.466s',
'2016-09-15 21:00:00.741 1.581s',
'2016-09-15 21:00:00.748 2.31s',
'2016-09-15 21:00:00.966 0.381s',
'2016-09-15 21:00:02.066 2.62s'
]
print(solution(lines))