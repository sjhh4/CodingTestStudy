def solution(clothes):
    answer = 1
    
    # print(clothes)
    ootd = {}
    for i in range(len(clothes)):
        if clothes[i][1] in ootd:
            ootd[clothes[i][1]].append(clothes[i][0])
        else:
            ootd[clothes[i][1]] = [clothes[i][0]]
    print(ootd)
    for i in ootd:
        answer *= len(ootd[i]) + 1
    print(answer - 1)
    return answer -1
    
    '''
    옛날 답안
    answer = 1
    fit = {}
    for i in range(len(clothes)):
        if clothes[i][1] in fit:
            fit[clothes[i][1]] += 1
        else:
            fit[clothes[i][1]] = 1
    print(fit)
    # print(len(fit))
    for i in fit:
        answer *= fit[i]+1
    print(answer-1)
    return answer-1
    '''
    '''
    프로그래머스 답안
    def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes]) # collection 모듈의 Counter 함수. 해당 인자의 개수를 세어 딕셔너리 키(인자), 밸류(횟수)의 형태로 반환
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1  # reduce(x1, x2, x3)는 반복 가능한 함수, 그 함수에 들어갈 변수, 변수가 존재 하지 않을때 대입할 값 의 형태로, map과 유사한 느낌
    return answer
    '''


solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]) # 5
solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])	# 3