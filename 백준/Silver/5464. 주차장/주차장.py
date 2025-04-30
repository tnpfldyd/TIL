import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
parking_rates = [int(input()) for _ in range(N)]
car_weights = [0] + [int(input()) for _ in range(M)]
events = [int(input()) for _ in range(2 * M)]

parking_lot = [None] * N
car_to_spot = dict()
wait_queue = deque()
total_income = 0

def find_empty_spot():
    for i in range(N):
        if parking_lot[i] is None:
            return i
    return -1

for event in events:
    if event > 0:
        car = event
        spot = find_empty_spot()
        if spot != -1:
            parking_lot[spot] = car
            car_to_spot[car] = spot
            total_income += parking_rates[spot] * car_weights[car]
        else:
            wait_queue.append(car)
    else:
        car = -event
        spot = car_to_spot[car]
        parking_lot[spot] = None
        del car_to_spot[car]
        if wait_queue:
            next_car = wait_queue.popleft()
            parking_lot[spot] = next_car
            car_to_spot[next_car] = spot
            total_income += parking_rates[spot] * car_weights[next_car]

print(total_income)