import itertools
def solution(users, emoticons):
    sale = [10, 20, 30, 40]
    result = [0, 0]
    for sales in itertools.product(sale, repeat=len(emoticons)):
        emoticon = []
        for i in range(len(emoticons)):
            emoticon.append(emoticons[i] - (emoticons[i] * sales[i] // 100))
        temp = [0, 0]
        for i in range(len(users)):
            users_temp = 0
            for j in range(len(emoticons)):
                if users[i][0] <= sales[j]:
                    users_temp += emoticon[j]
            if users_temp >= users[i][1]:
                temp[0] += 1
            else:
                temp[1] += users_temp
        if result[0] < temp[0]:
            result = temp
        elif result[0] == temp[0]:
            if result[1] < temp[1]:
                result = temp
    return result