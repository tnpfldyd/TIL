import sys
input = sys.stdin.readline

class Egg:
    def __init__(self, hp, weight):
        self.hp = hp
        self.weight = weight
    
    def attack(self, weight):
        self.hp -= weight
    
    def restore(self, weight):
        self.hp += weight

def back_tracking(cur):
    global answer

    if cur > N:
        return
    
    for i in range(N):
        if eggs[cur].hp <= 0:
            back_tracking(cur + 1)

        elif cur == i or eggs[i].hp <= 0:
            continue

        else:
            eggs[i].attack(eggs[cur].weight)
            eggs[cur].attack(eggs[i].weight)
            back_tracking(cur + 1)
            eggs[i].restore(eggs[cur].weight)
            eggs[cur].restore(eggs[i].weight)

    result = sum(1 for i in range(N) if eggs[i].hp <= 0)
    answer = max(answer, result)

N = int(input())
eggs = [Egg(*map(int, input().split())) for _ in range(N)] + [Egg(0, 0)]

answer = 0
back_tracking(0)

print(answer)