# 입력
# 10*10 크기의 미로 상자의 구조와 먹이의 위치가 입력된다.

# 출력
# 성실한 개미가 이동한 경로를 9로 표시해 출력한다.

# 입력 예시   
# 1 1 1 1 1 1 1 1 1 1
# 1 0 0 1 0 0 0 0 0 1
# 1 0 0 1 1 1 0 0 0 1
# 1 0 0 0 0 0 0 1 0 1
# 1 0 0 0 0 0 0 1 0 1
# 1 0 0 0 0 1 0 1 0 1
# 1 0 0 0 0 1 2 1 0 1
# 1 0 0 0 0 1 0 0 0 1
# 1 0 0 0 0 0 0 0 0 1
# 1 1 1 1 1 1 1 1 1 1

# 출력 예시
# 1 1 1 1 1 1 1 1 1 1
# 1 9 9 1 0 0 0 0 0 1
# 1 0 9 1 1 1 0 0 0 1
# 1 0 9 9 9 9 9 1 0 1
# 1 0 0 0 0 0 9 1 0 1
# 1 0 0 0 0 1 9 1 0 1
# 1 0 0 0 0 1 9 1 0 1
# 1 0 0 0 0 1 0 0 0 1
# 1 0 0 0 0 0 0 0 0 1
# 1 1 1 1 1 1 1 1 1 1

mirotic = []
for i in range(10): mirotic.append(list(map(int, input().split())))
i = 1
j = 1

while mirotic[i][j] != 2:
    if mirotic[i][j] == 9:
        break
    elif mirotic[i][j] == 0:
        mirotic[i][j] = 9
        if mirotic[i][j+1] != 1:
            j += 1
        else:
            if mirotic[i+1][j] != 1:
                i+=1
            else:
                break

mirotic[i][j] = 9
for a in range(10):
    for b in range(10):
        print(mirotic[a][b], end=' ')
    print(end='\n')






# def move(i, j):
#     if mirotic[i][j]==2:
#         mirotic[i][j] = 9
#         pri(mirotic)
#     else:
#         mirotic[i][j] = 9
#         if mirotic[i][j+1] != 1:
#             j+=1
#         elif mirotic[i][j+1] == 1:
#             if mirotic[i+1][j] !=1:
#                 i+=1
#             elif mirotic[i+1][j] == 1:
#                 pri(mirotic) 
        

# def pri(mirotic):
#     for i in range(10):
#         for j in range(10):
#             print(mirotic[i][j], end=' ')
#         print(end='\n')
#     return None

# move(i, j)