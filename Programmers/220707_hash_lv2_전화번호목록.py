import re

def solution(phone_book):
    # 마음에 드는 다른 사람 풀이
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    

    '''
    # 내 풀이는 실패
    shortnum = 99999999
    
    for i in phone_book:
        if len(i) < shortnum:
            shortword = i
            shortnum = len(i)
    print(shortword)
    for i in phone_book:
        if i == shortword:
            pass
        elif i.startswith(shortword):
            print('false')
            return 'false'
            pass
        else:
            pass
    print('true')c
    return 'true'
    '''

    return answer

solution(["119", "97674223", "1195524421"]) #	false
solution(["123","456","789"]) #	true
solution(["12","123","1235","567","88"]) #	false