def solution(mylist):
    answer = mylist[0]
    
    
    for i in range(len(mylist)):
        answer.append(len(mylist[i]))

    return answer


solution([[1, 2], [3, 4], [5]])