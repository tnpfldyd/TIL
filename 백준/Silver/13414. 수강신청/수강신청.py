import sys
input = sys.stdin.readline

K, L = map(int, input().split())
student_order = {}
for order in range(L):
    student_id = input().strip()
    student_order[student_id] = order
ordered_list = [(order, student_id) for student_id, order in student_order.items()]
ordered_list.sort()
for i in range(min(K, len(ordered_list))):
    print(ordered_list[i][1])