#큰단위순서로 잔돈을 거슬러주도록,,
changes = 1000 - int(input())
count = 0

for i in [500, 100, 50, 10, 5, 1]:
    count += changes // i
    changes %= i

print(count)