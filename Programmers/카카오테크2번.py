# from collections import deque

def solution(queue1, queue2):
    answer = 0
    a = 0
    b = 0
    # queue1 = deque(queue1)
    # queue2 = deque(queue2)
    qsum = int((sum(queue1) + sum(queue2))/2)
    uavg = qsum/len(queue1)

    if qsum in queue1:
        for i in range(queue1.index(qsum)+1):
            queue2.append(queue1.popleft())
            answer += 1
        for i in range(len(queue2)-1):
            queue1.append(queue2.popleft())
            answer += 1
    elif qsum in queue2:
        for i in range(queue2.index(qsum)+1):
            queue1.append(queue2.popleft())
            answer += 1
        for i in range(len(queue1)-1):
            queue2.append(queue1.popleft())
            answer += 1
    else:
        for i in range(len(queue1)*3):
            if sum(queue1) == qsum:
                break
            elif sum(queue1) > qsum:
                queue2.append(queue1.popleft())
                answer += 1
            else:
                queue1.append(queue2.popleft())
                answer += 1
        else:
            answer = -1
    
    # queue3 = queue1 + queue2
    # queue4 = queue2 + queue1
    # # print(len(queue3))
    # ex = 0
    # for i in range(len(queue1)+len(queue2)):
    #     if i < len(queue1):
    #         for j in range(len(queue3)-i):
    #             if sum(queue3[i:j+1]) != qsum:
    #                 pass
    #             else:
    #                 a = i
    #                 b = j
    #                 break
    #     else:
    #         for i in range(len(queue2)):
    #             for j in range(len(queue4)-i):
    #                 if sum(queue4[i:j+1]) != qsum:
    #                     pass
    #                 else:
    #                     a = i
    #                     b = j
    #                     break
    #     else:
    #         for i in range(len(queue2)):
    #             for j in range(len(queue4)-i):
    #                 if sum(queue4[i:j+1]) != qsum:
    #                     pass
    #                 else:
    #                     a = i
    #                     b = j
    #                     break
    # else:
    #     answer = -1

    # if a < len(queue1) and a+b < len(queue1):
    #     answer = a + 2*len(queue1)
    # # elif a < len(queue1) and a + b > len(queue1):
    # #     answer = 2*a + b+1-len(queue1)
    # # else:
    # #     answer  = -1
    # else:
    #     answer = 2*a + b+1-len(queue1)


    print(answer)
    return answer

solution([3, 2, 7, 2],[4, 6, 5, 1]) # 2
solution([1, 2, 1, 2], [1, 10, 1, 2]) # 7
solution([1, 1],[1, 5]) # -1