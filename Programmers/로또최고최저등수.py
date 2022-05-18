def solution(lottos, win_nums):
    answer = []
    
    setlot = set(lottos)
    setwin = set(win_nums)
    
    len(setlot & setwin)  # 최저 숫자 맞춘 개수 -> 최저등수
    
    #최고 등수
    #먼저 0의 개수를 알아야 함
    print(6-len(setlot)) # 0만 중복될 수 있으므로 6개 - set(win_nums)의 개수가 0의 개수가 됨.
    
    
    
    if len(setlot & setwin)+6-len(setlot) == 6:
        answer.append(1)
    elif len(setlot & setwin)+6-len(setlot) == 5:
        answer.append(2)
        
    elif len(setlot & setwin)+6-len(setlot) == 4:
        answer.append(3)
        
    elif len(setlot & setwin)+6-len(setlot) == 3:
        answer.append(2)
        
    elif len(setlot & setwin)+6-len(setlot) == 2:
        answer.append(1)


    if len(setlot&setwin) == 6:
        answer.append(1)
        
    elif len(setlot&setwin) == 5:
        answer.append(2)
    elif len(setlot&setwin) == 4:
        answer.append(3)
        
    elif len(setlot&setwin) == 3:
        answer.append(4)
        
    elif len(setlot&setwin) == 2:
        answer.append(5)

        
        
    return answer

solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])
solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])
solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])