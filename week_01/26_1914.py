'''
문제 설명
하노이 탑에는 세 개의 장대가 있습니다.
첫 번째 장대에 크기가 서로 다른 원판 N개가 작은 원판부터 큰 원판 순서로 쌓여 있습니다.
다음 규칙을 지키면서 모든 원판을 세 번째 장대로 옮기세요.
한 번에 원판 하나만 옮길 수 있습니다.
큰 원판을 작은 원판 위에 올릴 수 없습니다.
원판을 옮기는 최소 횟수와 이동 순서를 출력해야 합니다.

입력
첫째 줄에 원판의 개수 N이 주어집니다.
예시:
3

출력
첫째 줄에 최소 이동 횟수를 출력합니다.
N이 20 이하라면, 둘째 줄부터 각 원판을 옮긴 과정을 출력합니다.
각 이동은 다음 형식입니다.
출발 장대 도착 장대
예시:
7
1 3
1 2
3 2
1 3
2 1
2 3
1 3
'''

import sys
input = sys.stdin.readline

def hanoi(n, start, mid, end):
    if n == 1:
        print(start, end)
        return
    hanoi(n - 1, start, end, mid)
    print(start, end)
    hanoi(n - 1, mid, start, end)

n = int(input())

print(2 ** n - 1)

if n <= 20:
    hanoi(n, 1, 2, 3)