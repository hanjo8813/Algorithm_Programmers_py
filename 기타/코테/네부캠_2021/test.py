def solution(param0):

    answer = '........'
    base = '........'
    for idx, type in enumerate(param0):
        if type == 'BOOL':
            if answer[-1] == ',':
                answer += answer + base
            for i in range(len(answer), 0, -1):
                if answer[i] == '#' or answer[i] == ',':
                    answer[i+1] = '#'
                    continue
                if i == 0:
                    answer[i] = '#'
                    continue
        elif type == 'SHORT':
            if param0[idx-1] == 'BOOL':
                if answer[-1]
                for i in range(len(answer), 0, -1):
                    
                
            


        elif type == 'FLOAT':

        elif type == 'INT':

        elif type == 'LONG':
            answer +



    return