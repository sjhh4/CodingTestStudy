from collections import deque

def solution(priorities, location):
    answer = 1
    priorities = deque(priorities)
    # want = priorities[location]
    
    while True:
        if priorities[0] < max(priorities):
            if location != 0:
                priorities.append(priorities.popleft())
                location -= 1
            else:
                priorities.append(priorities.popleft())
                location = len(priorities)-1
        else:
            if location == 0:
                print(answer)
                return answer
            else:
                priorities.popleft()
                answer += 1
                location -= 1


solution([2, 1, 3, 2], 2) # 1
solution([1, 1, 9, 1, 1, 1], 0) #	5