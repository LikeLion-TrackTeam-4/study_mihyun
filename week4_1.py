# N = 트럭의 갯수
# W = 다리길이
# L = 최대하중
# 트럭무게 = [7, 4, 5, 6]

# 큐 초기화 > 첫번째 트럭 삽입 > 다음 트럭 합이 10이상이면 0삽입 > 7빼고 4넣기 > 4 + 5 는 10이하 5넣기 > 4빼고 +6은 10이상 0삽입
# 5빼고 6넣기 > 트럭없지만 6까지 빼야하니까 큐가 비도록 빼기.

#큐초기화,

import sys
from collections import deque

input = sys.stdin.readline

n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))
trucks.reverse() # 뒤집..

q = deque()
# 초기화
tot = 0 # 다리에 올라온 트럭무게
t = 0

while True:
    if len(trucks) == 0 and tot == 0:
        break

    # q의갯수와 다리길이의 값이 같으면 q에서 값 빼,,
    if len(q) == w:
        x = q.popleft()
        tot -= x

    # 뺐으면 넣기
    if len(trucks) > 0 and tot + trucks[-1] <= l:
        q.append(trucks[-1])
        tot += trucks[-1]
        trucks.pop()
    else:
        q.append(0)

    t += 1

print(t)