"""
5
""" 
N = 7
gom = 0
log_list = [
    "ENTER",
    "pjshwa",
    "chansol",
    "chogahui05",
    "ENTER",
    "pjshwa",
    "chansol",
]
list_ = list()
set_ = set()
for log in log_list:
    if log == "ENTER":
        list_.clear()

    else:
        # 닉네임 = log
        # 리스트에서 중복을 탐색할 때는 N 만큼의 시간이 필요합니다.
        # 셋에서 중복을 탐색할 때는 1 만큼의 시간이 필요합니다.
        if log not in list_:
            list_.add(log)
            gom += 1

print(gom)