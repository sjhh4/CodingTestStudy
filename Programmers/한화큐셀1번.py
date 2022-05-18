def solution(reqs):
    answer = []
    account = {}
    '''
    계좌 개설 요청: CREATE 계좌아이디 최대한도
    이미 개설된 계좌라면 403 코드를 보냅니다.
    개설되지 않은 계좌라면 -최대한도까지 출금할 수 있는 계좌를 개설한 후, 200 코드를 보냅니다.
    입금 요청: DEPOSIT 계좌아이디 금액
    없는 계좌라면 404 코드를 보냅니다.
    있는 계좌라면 금액 만큼을 입금한 후 200 코드를 보냅니다.
    출금 요청: WITHDRAW 계좌아이디 금액
    없는 계좌라면 404 코드를 보냅니다.
    계좌가 있지만, 최대한도를 초과한다면 출금을 하지 않고 403 코드를 보냅니다.
    그 외의 경우 계좌에서 금액 만큼을 출금 후 200 코드를 보냅니다.
    '''

    for i in range(len(reqs)):
        a, b, c=reqs[i].split(' ')
        c = int(c)
        if a.startswith('C'): # 계좌 생성
            if b in account: # 계좌가 있으면 403에러 코드
                answer.append(403)
            else: # 계좌가 없으면 계좌 생성
                account[b] = c
                answer.append(200)
        if a.startswith('D'): # 입금
            if b in account: # 계좌가 있는지 먼저 체크
                # 계좌가 있다면 입금
                account[b] += c
                answer.append(200)
            else: # 계좌가 없다면 
                answer.append(404)
        if a.startswith('W'): # 출금 요청
            if b in account: # 계좌가 있는지 체크
                if account[b] >= c: # 계좌가 있고, 최대한도가 충분한 경우
                    account[b] -= c
                    answer.append(200)
                else: # 계좌가 있지만, 최대한도를 넘은 경우
                    answer.append(403)
            else: # 계좌가 없는 경우
                answer.append(404)
    print(reqs)
    print(account)
    print(answer)
    return answer


solution(["DEPOSIT 3a 10000", "CREATE 3a 300000", "WITHDRAW 3a 150000", "WITHDRAW 3a 150001"]) # [404, 200, 200, 403]
solution(["CREATE 3a 10000", "CREATE 3a 20000", "CREATE 2bw 30000"]) # [200, 403, 200]