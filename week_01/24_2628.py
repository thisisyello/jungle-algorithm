'''
문제 설명
가로 길이와 세로 길이가 주어진 직사각형 종이가 있습니다.
이 종이를 여러 번 가로 또는 세로 방향으로 자릅니다.
모든 자르기가 끝난 뒤 만들어진 조각들 중에서 가장 넓은 조각의 넓이를 구하세요.

입력
첫째 줄에 종이의 가로 길이와 세로 길이가 주어집니다.
둘째 줄에 자르는 횟수 N이 주어집니다.
그다음 N개의 줄에는 자르는 방향과 위치가 주어집니다.
0 위치 → 가로 방향으로 자름
1 위치 → 세로 방향으로 자름
예시:
10 8
3
0 3
1 4
0 2

출력
잘린 종이 조각 중 가장 넓은 조각의 넓이를 출력합니다.
예시:
30
'''

import sys
input = sys.stdin.readline

x, y = map(int, input().split())
x_cuts = [0, x]
y_cuts = [0, y]
max_width = 0
max_height = 0
n = int(input())

for _ in range(n):
    way, location = map(int, input().split())
    if way == 1:
        x_cuts.append(location)
    else:
        y_cuts.append(location)

x_cuts.sort()
y_cuts.sort()

for i in range(len(x_cuts) - 1):
    if max_width <= x_cuts[i + 1] - x_cuts[i]:
        max_width = x_cuts[i + 1] - x_cuts[i]
        
for i in range(len(y_cuts) - 1):
    if max_height <= y_cuts[i + 1] - y_cuts[i]:
        max_height = y_cuts[i + 1] - y_cuts[i]

print(max_width * max_height)