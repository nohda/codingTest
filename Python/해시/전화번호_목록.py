# def solution(phone_book):
#     answer = True
#     phone_book.sort()
#     for i in range(len(phone_book)):
#         j = i + 1
#         while j < len(phone_book):
#             if phone_book[i] == phone_book[j][:len(phone_book[i])]:
#                 answer = False
#                 break;
#             j += 1
#     return answer

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i,j in zip(phone_book, phone_book[1:]):
        print(i,j,phone_book[1:])
        if i == j[:len(i)]:
            answer = False
        break;
    return answer

phone_book = ["12","123","1235","567","88"]
solution(phone_book)
