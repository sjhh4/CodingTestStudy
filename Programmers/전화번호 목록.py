# def solution(phone_book):
#     answer = True
    
#     for i in range(len(phone_book)-1):
#         for j in range(i+1, len(phone_book)):
#             if len(phone_book[i]) > len(phone_book[j]):
#                 if phone_book[i].startswith(phone_book[j]):
#                     answer = False
#                     break
#                 else:
#                     pass
#             elif len(phone_book[i]) < len(phone_book[j]):
#                 if phone_book[j].startswith(phone_book[i]):
#                     answer = False
#                     break
#                 else:
#                     pass
#             else:
#                 if phone_book[i] == phone_book[j]:
#                     answer = False
#                     break
#                 else:
#                     pass
            
            
            
#     #         phone_book[i].startswith(phone_book[j]) or phone_book[j].startswith(phone_book[i]):
#     #             answer = False
#     #         else:
#     #             pass
#     print(answer)
#     return answer

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    else:
        return True

solution(["119", "97674223", "1195524421"])	# false
solution(["123","456","789"]) # true
solution(["12","123","1235","567","88"]) # false