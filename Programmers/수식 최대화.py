def solution(expression):
    answer = 0
    ex2=[]
    ex3=[]
    ex = expression.split('+')
    for i in range(len(ex)-1):
        ex.insert(i+1, '+')
    # print(ex)
    for i in range(len(ex)):
        ex2+=ex[i].split('-')
    # for i in range(len(ex2)-1):
    #     ex2.insert(i+1, '-')
    for i in range(len(ex2)):
        ex3 += ex2[i].split('*')
    # for i in range(len(ex3)):
    #     ex3.insert(i+1, '*')
    print(ex3)
    print(type(ex3))


solution("100-200*300-500+20") # 60420
solution("50*6-3*2") # 300