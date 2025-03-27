import sys
input = sys.stdin.readline

S, E, Q = input().split()
start_time = int(S[:2]) * 60 + int(S[3:])
end_time = int(E[:2]) * 60 + int(E[3:])
quit_time = int(Q[:2]) * 60 + int(Q[3:])

enter = set()
attend = set()

while True:
    try:
        time, name = input().split()
        minutes = int(time[:2]) * 60 + int(time[3:])
        
        if minutes <= start_time:
            enter.add(name)
        elif minutes >= end_time and minutes <= quit_time:
            if name in enter:
                attend.add(name)
    except:
        break

print(len(attend))