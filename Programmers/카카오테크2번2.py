from collections import deque

def solution(queue1, queue2):
    answer = []
    a = -1
    b = -1
    c = []
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    qsum = int((sum(queue1) + sum(queue2))/2)
    uavg = qsum/len(queue1)

    queue3 = queue1 + queue2
    queue4 = queue2 + queue1
    
    for i in range(len(queue1)):
        for j in range(len(queue3)-i):
            if sum(queue3[i:j+i+1]) != qsum:
                pass
            else:
                a = i
                b = j
                c.append([0, a, b])
                # print('첫번째 경우. a =', a, 'b =', b)
                break
    else:
        for i in range(len(queue2)):
            for j in range(len(queue2)-i):
                if sum(queue4[i:j+i+1]) != qsum:
                    pass
                else:
                    a = i
                    b = j
                    # print('두번째 경우. a =', a, 'b =', b)
                    c.append([1, a, b])
                    break
    
    print(c, len(c))
    if len(c)==0:
        answer.append(-1)
    else:
        for i in range(len(c)):
            if c[i][0] == 0:
                if c[i][1]+c[i][2] >= len(queue1):
                    answer.append(2*c[i][1]+c[i][2]+1-len(queue1))
                elif c[i][1]+c[i][2] < len(queue1):
                    answer.append(2*c[i][1]+c[i][2]+1-len(queue2))
            elif c[i][0] == 1:
                if c[i][1]+c[i][2] >= len(queue1):
                    answer.append(2*c[i][1]+c[i][2]+1-len(queue1))
                elif c[i][1]+c[i][2] < len(queue1):
                    answer.append(2*c[i][1]+c[i][2]+1+len(queue2))

    print(answer, min(answer))
    return min(answer)

solution([3, 2, 7, 2],[4, 6, 5, 1]) # 2
solution([1, 2, 1, 2], [1, 10, 1, 2]) # 7
solution([1, 1],[1, 5]) # -1