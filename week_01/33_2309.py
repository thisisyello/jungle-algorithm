'''
문제 설명
아홉 명의 난쟁이의 키가 주어집니다.
이 중 실제 일곱 난쟁이의 키의 합은 정확히 100입니다.
아홉 명 중에서 실제 일곱 난쟁이를 찾아 키를 오름차순으로 출력하세요.

입력
아홉 줄에 걸쳐 난쟁이들의 키가 하나씩 주어집니다.
예시:
20
7
23
19
10
15
25
8
13

제한
난쟁이 수 = 9명
각 키 ≤ 100
주어지는 키는 모두 다름
정답은 여러 개일 수 있음

출력
실제 일곱 난쟁이의 키를 오름차순으로 한 줄에 하나씩 출력합니다.
정답이 여러 개인 경우 아무거나 출력하면 됩니다.
예시:
7
8
10
13
19
20
23
'''

import sys
input = sys.stdin.readline

heights = []

for _ in range(9):
    h = int(input())
    heights.append(h)

total = sum(heights)

a = 0
b = 0
founds = False

for i in range(len(heights)):
    for j in range(i + 1, len(heights)):
        if heights[i] + heights[j] == total - 100:
            a = heights[i]
            b = heights[j]
            founds = True
            break
    if founds:
        heights.remove(a)
        heights.remove(b)
        break

heights.sort()
print('\n'.join(map(str, heights)))
