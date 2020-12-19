def solution(files):
    s_files = []
    for i, f in enumerate(files):
        flag = cnt = 0
        head = number = ''
        s_files.append([f])
        for j in range(len(f)):
            # head
            if flag == 0:
                if str(f[j]).isdigit() == 0:
                    head += f[j]
                else :
                    s_files[i].append(head.lower())
                    flag+=1
            # number
            else :
                cnt += 1
                if str(f[j]).isdigit()==1:
                    if flag == 1:
                        if f[j] == '0':
                            continue
                        else:
                            flag+=1
                    number += f[j]
                if str(f[j]).isdigit()==0 or cnt == 4 or j == len(f)-1:
                    s_files[i].append(number)
                    break
                
                

    print(s_files)
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

