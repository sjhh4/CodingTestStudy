def solution(participant, completion):
    # answer = []

    hash = {}
    for i in participant:
        hash[i] = hash.get(i, 0) + 1
    # print(hash)
    for i in completion:
        hash[i] -= 1

    # print(hash)

    for k, v in hash.items():
        if v != 0:
            answer = k
    print(answer)

    '''
    옛날 답안
    
    answer = ''
    
    dictpar = dict()
    dictcom = dict()
       
    for i in participant:
        if i in dictpar:
            dictpar[i] += 1
        else:
            dictpar[i] = 1
        
        
    for i in completion:
        if dictpar[i]==1 :
            del dictpar[i]
        else : 
            dictpar[i] -=1
    
    answer = list(dictpar.keys())[0]
    
    setpart = set(participant)
    setcomp = set(completion)
    fail = setpart - setcomp
    fail = list(fail)
    answer = fail

    '''
    return answer

solution(["leo", "kiki", "eden"], ["eden", "kiki"])	# "leo"
solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]) # "vinko"
solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]) # "mislav"