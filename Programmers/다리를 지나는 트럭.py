from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    ongoing = dict()
    onweight = 0
    
    while len(ongoing)!=0 or len(truck_weights)!=0:

        answer += 1 # update int answer

        if len(truck_weights) != 0:
            if len(ongoing) <= bridge_length and onweight <= weight:
                print(answer)
                onweight += truck_weights[0]
                ongoing[truck_weights.popleft()] = bridge_length # update dict ongoing
            else:
                pass
        else:
            pass

        if len(ongoing) != 0:
            for i in ongoing:
                if ongoing[i] != 0: 
                    ongoing[i] -= 1 # update dict ongoing
                else:
                    onweight -= ongoing[i] # update int onweight
                    del ongoing[i]
        else:
            pass



    print(answer)
    return answer

'''
구글링 해서 찾은 답
from collections import deque

def solution(bridge_length, weight, truck_weights):
    tasks = deque([x for x in truck_weights])
    proc = deque([0 for _ in range(bridge_length)])	# 1
    time = stack = 0
    
    while proc:
        if proc[0] > 0:	# 2
            stack -= proc[0]
            
        time += 1	# 3
        proc.popleft()
        
        if tasks:
            if (stack + tasks[0]) <= weight:	# 4
                stack += tasks[0]
                proc.append(tasks.popleft())	# 5
            else:
                proc.append(0)	# 6
        
    return time
'''

'''환형 큐(circular que) 고려해보기
collections의 rotate 함수 써서'''

solution(2, 10, [7,4,5,6]) # 8
solution(100, 100, [10]) # 101
solution(100, 100, [10,10,10,10,10,10,10,10,10,10]) # 110