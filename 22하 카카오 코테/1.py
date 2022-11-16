def solution(box):
    # Write your code here
    """
    보아하니 상자 속 빵을 disperse 하는게 핵심인데, 문제는 i번째 박스에서 i-1번째 박스로 밖에 분배 못함 (일방향적)
    즉, 아래 방향으로 흘러내려가야 함
    
    가장 이상적인 상황은 박스 속 빵의 갯수의 평균만큼 좌르륵 분배시키는 것!
    point는 일방향적 분배이기 때문에
    가장 높은 번호의 박스 속 빵의 개수가
    본인을 포함한 이하의 모든 박스의 빵 개수의 평균보다 많아야 분배가 시작**
    
    즉, 분배를 시작할 수 있는 박스를 기준으로 빵의 개수의 평균만 찾으면 바로 max값을 찾을 수 있음.
    
    처리해야 할 예외 케이스
    가장 번호가 큰 박스의 빵 개수가 적은 경우 o
    평균이 정수가 아닌 경우
    1번 박스에 많은 빵이 있는 경우 o
    """
    
    l = len(box)
    total = sum(box)
    avg = total/l # 계속 바뀌어야 할 변수
    print(box, total, avg)
    
    for i in range(l):
        avg = sum(box[:l-i])/(l-i)
        print(i,box[:l-i], sum(box[:l-i]), l-i, avg)
        # if box[0] > avg:
        #     return box[0]
        # elif box[l-i-1] < avg:
        #     pass
        # elif box[l-i-1] > avg:
        #     if avg == int(avg):
        #         return int(avg)
        #     else:
        #         return int(avg) + 1
        # else:
        #     flow = box[l-1-i] - int(avg)
        #     box[l-1-i] -= flow
        #     box[l-2-i] += flow
        #     # return int(sum(box[:l-i])/l-i)
        #     return max(box)


solution([3, 8, 11, 7])