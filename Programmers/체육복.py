def solution(n, lost, reserve):
    answer = 0
    dictn = dict()
    # dictl = dict()
    # dictr = dict()
    
    for i in range(1, n+1):
        dictn[i] = 1
    
    for i in lost:
        dictn[i] -= 1
        
    for i in reserve:
        dictn[i] += 1
    
    print(dictn)


    for i in range(1, n+1):
        if i == 1:
            if dictn[i] != 0:
                pass
            else:
                if dictn[i+1]!=2:
                    pass
                else:
                    dictn[i] += 1
                    dictn[i+1] -= 1
        elif i == n:
            if dictn[i] != 0:
                pass
            else:
                if dictn[i-1]!=2:
                    pass
                else:
                    dictn[i] += 1
                    dictn[i-1] -= 1
        else:
            if dictn[i] !=0:
                pass
            elif dictn[i] == 0:
                if dictn[i-1] == 2:
                    dictn[i-1] -=1
                    dictn[i] +=1
                elif dictn[i+1] == 2:
                    dictn[i] +=1
                    dictn[i+1] -=1
                else:
                    pass
    
    for i in range(1, n+1):
        if dictn[i] != 0:
            answer +=1
        else:
            pass



    return answer

solution(5, [2, 4], [1, 3, 5])
solution(5, [2, 4], [3])
solution(3, [3],[1])