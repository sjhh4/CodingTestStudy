def solution(genres, plays):
    answer = []
    # 나의 잘못된 풀이
    goat = {}

    for i, j in enumerate(zip(genres, plays)):
        if j[0] not in goat:
            goat[j[0]] = {i : j[1]}
        else:
            goat[j[0]][i] = j[1]
    print(goat)

    print(max(goat))
    print(max(goat[max(goat)]))
    for i in range(len(goat)):
        origin = max(goat)
        for j in range(2):
            answer.append(max(goat[origin]))
            # del goat[origin][max(goat[origin])]
            if j == 1:
                del goat[origin]
            else:
                del goat[origin][max(goat[origin])]
    print('answer is ',answer)
    

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




solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]) # [4, 1, 3, 0]