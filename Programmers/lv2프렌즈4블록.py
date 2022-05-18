def solution(m, n, board):
    answer = 0

    '''
    내 풀이

    for문 두개를 통해 한 블록을 기준으로 아래, 오른쪽, 오른쪽 아래와 같은지 체크
    -> 그리고 각각의 블록을 기준으로 다시 똑같이 체크
    그렇게 해서 같은게 확인된 것은 기준된 블록을 candidate에 위치정보를 저장.

    블록에 있는 것을 삭제하고 삭제된 블록의 개수를 answer에 더해줌.
    위에 행의 블록을 대체 (replace함수 써서)
    위에 행의 블록이 없다면 pass


    '''
    candidate =[]


    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j] and board[i][j] == board[i+1][j+1]:
                candidate.append('')
                '변수. replace(old, new, [count])'
                board[i].replace(board[i][j], O)
                board[i+1].replace(board[i][j], O)
                


    
    return answer








solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])
solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])