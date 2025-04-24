def count_valid_skills(n, skills):
    result = 0
    l_ready = 0
    s_ready = 0
    broken = False

    for skill in skills:
        if broken:
            break
        if skill in "123456789":
            result += 1
        elif skill == 'L':
            l_ready += 1
        elif skill == 'S':
            s_ready += 1
        elif skill == 'R':
            if l_ready:
                result += 1
                l_ready -= 1
            else:
                broken = True
        elif skill == 'K':
            if s_ready:
                result += 1
                s_ready -= 1
            else:
                broken = True

    return result

n = int(input())
skills = input().strip()
print(count_valid_skills(n, skills))