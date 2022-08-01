N, M = list(map(int, input().split()))
cnt = 0
for i in range(M):
    book = int(input())
    book_numbers = list(map(int, input().split()))
    for j in range(book-1): # 책이 2권일 경우 1번만 확인하면 됨. 3번일 경우 2번
        if book_numbers[j] < book_numbers[j+1]: # 첫번째 번호가 두번째 보다 커야하는데, 작을 경우
            cnt += 1
print('Yes' if cnt == 0 else 'No')
