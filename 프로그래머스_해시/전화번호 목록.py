def solution(phone_book):
    phone_book.sort(key=lambda x: -len(x))
    print(phone_book)
    for x in phone_book:
        temp = ""
        for y in x:
            temp += y
            if temp == x:
                break
            if temp in phone_book:
                return False
    return True

if __name__ == "__main__":
    phone_book = ['119', '97674223', '1195524421']
    print(solution(phone_book))

'''
def solution(phone_book):
    answer = True
    #정렬
    phone_book.sort()
    #zip 쌍 지어줌. 두 리스트 동시에 증가하면서 비교할 때...
    for p1,p2 in zip(phone_book,phone_book[1:]):
        #startswith
        if p2.startswith(p1):
            answer = False
            break
    return answer
'''