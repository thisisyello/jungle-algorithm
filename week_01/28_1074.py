'''
문제 설명
크기가 2^N x 2^N인 배열을 Z 모양으로 탐색합니다.
탐색 순서는 다음과 같습니다.
왼쪽 위
오른쪽 위
왼쪽 아래
오른쪽 아래
배열이 더 크면 네 구역으로 나눈 뒤, 각 구역 안에서도 다시 같은 Z 순서로 탐색합니다.
주어진 좌표 (r, c)가 몇 번째로 방문되는지 구하세요.

입력
첫째 줄에 정수 N, r, c가 공백으로 구분되어 주어집니다.
예시:
2 3 1

출력
좌표 (r, c)가 방문되는 순서를 출력합니다.
방문 순서는 0부터 시작합니다.
예시:
11
'''

import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

size = 2 ** n
answer = 0

def z_order(size, row, col):
    if size == 1:
        return 0

    half = size // 2
    area = half * half

    # 1사분면: 왼쪽 위
    if row < half and col < half:
        return z_order(half, row, col)
    # 2사분면: 오른쪽 위
    elif row < half and col >= half:
        return area + z_order(half, row, col - half)
    # 3사분면: 왼쪽 아래
    elif row >= half and col < half:
        return 2 * area + z_order(half, row - half, col)

    # 4사분면: 오른쪽 아래
    return 3 * area + z_order(half, row - half, col - half)

print(z_order(size, r, c))