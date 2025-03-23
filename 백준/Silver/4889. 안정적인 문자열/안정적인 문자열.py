import sys

def min_operations(s):
    balance = 0
    operations = 0
    
    for char in s:
        if char == '{':
            balance += 1
        else:
            balance -= 1
            if balance < 0:
                operations += 1
                balance = 1
    
    if balance > 0:
        operations += balance // 2
    
    return operations

case_num = 1
for line in sys.stdin:
    s = line.strip()
    if s.startswith('-'):
        break
    print(f"{case_num}. {min_operations(s)}")
    case_num += 1