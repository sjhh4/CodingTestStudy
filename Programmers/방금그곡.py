from time import time

def solution(m, musicinfos):
    answer = ''
    
    song = dict()
    
    for i in range(len(musicinfos)):
        a, b, c, d = musicinfos[i].split(',')
        atemp = int(a[:2])
        a = int(a[3:])
        a += atemp*60
        btemp = int(b[:2])
        b = int(b[3:])
        b += btemp * 60
        song[i] = {'start':a, 'end': b, 'note': d, 'name':c}
        print(song)

    for i in range(len(musicinfos)):
        if m in song[i]['note']*(song[i]['end']-song[i]['start']):
            answer += song[i]['name']


    return answer


solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])