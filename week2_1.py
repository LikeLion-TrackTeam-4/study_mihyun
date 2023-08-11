#에디터 1406

from sys import stdin

l = list(input())
r = []

for _ in range(int(input())):
    str = list(stdin.readline().split())
    if str[0] == 'L' and l:
        r.append(l.pop())
    elif str[0] == 'D' and r:
        l.append(r.pop())
    elif str[0] == 'B' and l:
        l.pop()
    elif str[0] == 'P':
        l.append(str[1])

answer = l + r[::-1]
print(''.join(answer))
