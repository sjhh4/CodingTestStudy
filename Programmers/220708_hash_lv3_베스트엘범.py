def solution(genres, plays):
    answer = []
    # 나의 잘못된 풀이
    # 같은 장르의 음악의 총 재생수를 기준으로 최대 장르를 구해야 하는데, 단일곡 기준 최대 재생곡의 장르를 생각함.
    # goat = {}

    # for i, j in enumerate(zip(genres, plays)):
    #     if j[0] not in goat:
    #         goat[j[0]] = {i : j[1]}
    #     else:
    #         goat[j[0]][i] = j[1]
    # print(goat)
    
    # print(max(goat))
    # print(max(goat[max(goat)]))
    # for i in range(len(goat)):
    #     origin = max(sum(goat[:]))
    #     for j in range(2):
    #         answer.append(max(goat[origin]))
    #         # del goat[origin][max(goat[origin])]
    #         if j == 1:
    #             del goat[origin]
    #         else:
    #             del goat[origin][max(goat[origin])]
    # print('answer is ',answer)
    
    total_play = {}
    ingenre = {}
    for i, j in zip(genres, plays):
        if i in total_play:
            total_play[i] += j
        else:
            total_play[i] = j

    print(genres, plays)
    print(total_play)
    for i in set(genres):
        ingenre[i] = []
    for i in range(len(genres)):
        ingenre[genres[i]] += [(i, plays[i])]
    print(ingenre)
    for i in ingenre:
        i.sort(key = lambda x: x[1], reverse = True)
        
    return answer

    '''
    스터디원 동현씨 답변
    def solution(genres, plays):
    answer = []
    play_dict = {}
    total_dict = {}

    for i in range(len(genres)) :
        play_dict[genres[i]] = play_dict.get(genres[i], 0) + plays[i]
        total_dict[genres[i]] = total_dict.get(genres[i], []) + [(plays[i], i)]


    play_sort = sorted(play_dict.items(), key = lambda x: x[1], reverse = True)

    for genre, play in play_sort :
        total_dict[genre] = sorted(total_dict[genre], key = lambda x: x[0], reverse = True)
        answer += [idx for play, idx in total_dict[genre][:2]]

    return answer
    '''

    '''
    enumerate 함수는 for i in enumerate(인자):
    돌때 i는 (n번째, n번쨰 인자) 형식으로 반환
    zip 함수는 for i,j in zip(인자1, 인자2):
    돌때 i는 인자1의 n번째, j는 인자2의 n번째

    list의 합(+)은 리스트 뒤에 리스트 형식으로 붙음
    ex) [1, 2, 3] + [2, 3, 4] => [1, 2, 3, 2, 3, 4]

    hash table(딕셔너리) 만들때에는 get함수 무조건 쓴다고 생각!
    크기 순서대로 정렬하기 힘들다?!  ->  정렬하고 싶은 데이터(주로 hash table의 value값)를
    list 형태로 만들어서 .sort(reverse = True), sorted(인자, ket = 정렬할 기준(ex 람다함수),reverse = True) 생각하기!

    lamda 함수 공부하기!

    넣고 정렬하는게 힘들면, 정렬하고 넣는것을 생각한다!

    '''



solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]) # [4, 1, 3, 0]