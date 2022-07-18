number_list = [1, 23, 9, 6, 91, 59, 29]
high = max(number_list) #함수의 이름을 변수로 지정함.

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
high2 = max(number_list2) #그러다 보니 아래 코드에선 함수가 적용이 된것이 아닌 변수의 이름이 적용됨.

if high > high2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif high < high2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")