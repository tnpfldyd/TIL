from math import remainder


a = int(input())

b = 0

while a:
    b += a % 10
    a //= 10
print(b)

# while a:
#     a, remainder(나머지) = divmod(a, 10) - 몫과 나머지를 튜플로 구하는 함수
#     b += remainder(나머지)
# print(b)