def solution(participant, completion):
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
    
    # setpart = set(participant)
    # setcomp = set(completion)
    # fail = setpart - setcomp
    # fail = list(fail)
    # answer = fail
    return answer


solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])