# 1. 기본
# input이 1 2 일때, 
# numbers는 리스트이다. ['1', '2']
# numbers = input().split()
# a = int(numbers[0])
# b = int(numbers[1])
# print(a)
# print(b)

# 2. 결과를 동시에 할당
# input이 1 2 일때,
# a는 '1'
# b는 '2'
# a, b = input().split() 
# print(int(a))
# print(int(b))

# 3. 고~~급 방법 => 수요일에 떠 먹여드립니다!
a, b = map(int, input().split())
print(a, type(a))
print(b, type(b))