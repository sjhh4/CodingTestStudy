def solution(survey, choices):
    answer = ''
    chardict = {'R': 0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}

    print(survey)
    print(choices)
    for i in range(len(choices)):
        if choices[i]==4:
            pass
        elif choices[i]==1:
            chardict[survey[i][0]] += 3
        elif choices[i]==2:
            chardict[survey[i][0]] += 2
        elif choices[i]==3:
            chardict[survey[i][0]] += 1
        elif choices[i]==5:
            chardict[survey[i][1]] += 1
        elif choices[i]==6:
            chardict[survey[i][1]] += 2
        else:
            chardict[survey[i][1]] += 3
    
    print(chardict.items())
    tupanswer = tuple(chardict.items())
    for i in range(4):
        if tupanswer[2*i][1] >= tupanswer[2*i+1][1]:
            answer += tupanswer[2*i][0]
        else:
            answer += tupanswer[2*i+1][0]
        
    print(answer)

    return answer




solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5])	# "TCMA"
solution(["TR", "RT", "TR"],[7, 1, 3])	# "RCJA"