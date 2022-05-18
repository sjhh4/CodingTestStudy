from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    a=0
    b = 0
    while len(progresses) != 0:
        b+=1
        if  b == 100:
            break
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
        # print(progresses)
        if progresses[0] >= 100:
            for i in range(len(progresses)):
                if progresses[i] >= 100:
                    a = i+1
                else:
                    break
            for i in range(a):
                progresses.popleft()
                speeds.popleft()
            
        if a !=0:
            answer.append(a)
            a = 0
    print(answer)
    return answer


solution([93, 30, 55], [1, 30, 5]) # [2, 1]
solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]) # [1, 3, 2]