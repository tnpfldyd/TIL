list_ = [[1, 2, 4],
         [8, 16, 32]]

i, j, x, y = 1, 1, 2, 2

i -= 1
j -= 1
x -= 1
y -= 1

sum_ = 0
# 이중 반복문
# i -> x
for r in range(i, x+1):
    # j -> y
    for c in range(j, y+1):
        sum_ += list_[r][c] 

print(sum_)

# 파이썬 제출
# python3 : 메모리 사용이 적고, 속도가 느려요.
# pypy3 : 메모리 사용이 많은데 속도가 빨라요. 