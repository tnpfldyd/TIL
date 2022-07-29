import sys
sys.stdin = open('10505input.txt', 'r')
T = int(input())
for i in range(1, T+1):
    person = int(input())
    pay = list(map(int, input().split()))
    average_pay = sum(pay) / person
    average_person = []
    for j in pay:
        if j <= average_pay:
            average_person.append(j)
    print(f'#{i}', len(average_person))