import sys
sys.stdin = open("1228input.txt", "r")

N = 10
for i in range(1, N+1):
    T = input()
    word = list(map(int, input().split()))
    case = int(input())
    init_ = input().split('I')
    init_ = list(filter(None, init_))
    for j in range(case):
        word_in = init_[j].split()
        word = word[:int(word_in[0])] + word_in[2:] + word[int(word_in[0]):]
    print(f'#{i}', *word[0:10])
