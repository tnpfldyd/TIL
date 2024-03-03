import sys
input = sys.stdin.readline

def find_tags(line):
    tags = []
    while '<' in line and '>' in line:
        start = line.index('<')
        end = line.index('>') + 1
        tags.append(line[start:end])
        line = line[end:]
    return tags

def is_legal_html(line):
    tags = find_tags(line)
    stack = []
    for tag in tags:
        if tag.startswith('</'):
            if not stack:
                return 'illegal'
            opening_tag = stack.pop()
            if '</' + opening_tag not in tag:
                return 'illegal'
        elif tag.endswith('/>'):
            continue
        else:
            tag_name = tag[1:].split()[0]
            if '/' in tag_name:
                tag_name = tag_name.split('/')[0]
            stack.append(tag_name)
    return 'legal' if not stack else 'illegal'

while True:
    line = input().strip()
    if line == '#':
        break
    print(is_legal_html(line))