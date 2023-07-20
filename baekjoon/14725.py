import sys
input = sys.stdin.readline

N = int(input())
ant_dic = {}

for _ in range(N):
    ants = list(input().split())[1:]
    target = ant_dic
    for ant in ants:
        if ant not in target:
            target[ant] = {}
        target = target[ant]

def getprint(dic, idx):
    keys = sorted(dic.keys())
    for key in keys:
        print('--' * idx + key)
        getprint(dic[key], idx + 1)
getprint(ant_dic, 0)

