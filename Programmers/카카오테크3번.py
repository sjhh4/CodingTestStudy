def solution(alp, cop, problems):
    answer = [alp, cop, 0] # 현재 상태의 alp, cop, 그리고 여태까지 공부하는데 걸린 시간
    quedict = dict()
    bhurdle = list() # 모든 문제를 풀기 위한 알고리즘, 코딩 능력 상승해야 할 최소치
    shurdle = list() # 풀 수 있는 문제 까지 필요한 알고리즘, 코딩 능력 상승해야 할 최소치
    for i in range(len(problems)):
        quedict[i] = {'alp_req':problems[i][0], 'cop_req':problems[i][1], 'alp_rwd':problems[i][2], 'cop_rwd':problems[i][3], 'cost':problems[i][4]}

    bhurdle.append(max(problems[i][0] for i in range(len(problems))))
    bhurdle.append(max(problems[i][1] for i in range(len(problems))))
    bhurdle[0] -= alp
    bhurdle[1] -= cop
    # print(bhurdle)
    k = 0
    smallq = 150

    if min(problems[i][0] for i in range(len(problems))) - answer[0] > 0 and min(problems[i][1] for i in range(len(problems))) - answer[1] > 0: # 코딩파워 알고파워로 아무 문제도 풀 수 없을 때 풀 수 있는 가장 첫 문제를 풀 수 있도록 공부하기
        for i in range(len(problems)):
            if smallq < problems[i][0]+problems[i][1]:
                pass
            if smallq > problems[i][0]+problems[i][1]:
                k = i
                smallq = problems[i][0]+problems[i][1]
            if smallq == problems[i][0]+problems[i][1]: # 가장 효율적인 문제 선택
                if problems[k][2] + problems[k][3] < problems[i][2]+problems[i][3]:
                    k = i
                    smallq = problems[i][0]+problems[i][1]
                else:
                    pass
        answer[2] += problems[k][0]+problems[k][1]
        answer[0] = problems[k][0]
        answer[1] = problems[k][1]

    elif min(problems[i][0] for i in range(len(problems))) - answer[0] > 0 and min(problems[i][1] for i in range(len(problems))) - answer[1] <= 0: # alp를 공부해야할 때
        pass
    elif min(problems[i][0] for i in range(len(problems))) - answer[0] <= 0 and min(problems[i][1] for i in range(len(problems))) - answer[1] > 0: # cop를 공부해야할 때
        pass
    
    print(answer)
        
        # if min(problems[i][0] for i in range(len(problems))) - answer[0] > min(problems[i][1] for i in range(len(problems))) - answer[1]:
        #     answer[1] += 1
        #     bhurdle[1] -= 1
        #     answer[2] += 1
        # if min(problems[i][0] for i in range(len(problems))) - answer[0] < min(problems[i][1] for i in range(len(problems))) - answer[1]:
        #     answer[0] += 1
        #     bhurdle[0] -= 1
        #     answer[2] += 1
        # if min(problems[i][0] for i in range(len(problems))) - answer[0] = min(problems[i][1] for i in range(len(problems))) - answer[1]:


    return answer[2]


solution(10,10,[[10,15,2,1,2],[20,20,3,3,4]]) # 15
solution(0,0,[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]) # 13