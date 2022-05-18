def solution(board, moves):
    answer = 0
    
    print(len(board))
    print(moves)
    nbyn = {}
    for i in range(len(board)):
        nbyn[i] = board[i]
    
    print(nbyn)
    
    for i in range(len(moves)):
        moveind = moves[i]-1
        print(moveind)
        if len(moves) != 0:
            if len(board[moveind]) !=0:
                if moves[-1] == board[moveind][-1]:
                    movepop = moves.pop()
                    print(movepop)
                    boardpop = board[moveind].pop()
                    print(boardpop)
                    answer +=1
                if moves[-1] != board[moveind][-1]:
                    moves.append(board[moveind].pop())
                
            if len(board[moveind]) == 0:
                pass
            
        if len(moves) == 0:
            if len(board[moveind]) !=0:
                moves.append(pop.board[moveind])
                
            if len(board[moveind]) == 0:
                pass
        

    '''
    구글링해서 찾은 답
    
    def solution(board, moves):
    basket = []
    now_doll = 1
    answer = 0
    
    for m in moves:
    
        if board[m-1]: #  만약 인형이 없는 곳에서 크레인을 작동시키는 경우에는 아무런 일도 일어나지 않습니다.
        
            step = True
            i = 0
            
            while step != False:
                if i >= len(board)-1: step = False
                
                now_doll = board[i][m-1]
                if now_doll != 0:
                # 리스트에 추가하기 전, 마지막 원소에 같은 num이 있는지 확인
                    if basket and now_doll == basket[-1]: # 존재한다면
                        basket.pop() # 같은 num을 가진 마지막 원소 제거
                        answer += 2 # 사라진 캐릭터 수 +2
                    else: basket.append(now_doll) # 존재하지 않는다면 basket에 추가
                    board[i][m-1] = 0 # basket으로 인형을 옮겼기 때문에 0으로 변경
                    step = False
                    
                i += 1
    return answer
    '''





    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])