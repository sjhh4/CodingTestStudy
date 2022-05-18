def solution(absolutes, signs):
    answer = 0
    preanswer = ''
    
    # str_signs = str(signs)
    # str_signs = ''.join(signs)
    
    # str_signs.replace('true', '+')
    # str_signs.replace('false', '-')
    
    for i, j in zip(signs, absolutes):
        if i == 'true':
            answer += j
        elif i == 'false':
            answer -= j


    return answer

signs = ['true','false','true']

print((solution([4,7,12], signs)))
# solution([1,2,3], [false,false,true])