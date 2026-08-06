'''
문제 설명
크기가 N x N인 체스판 위에 퀸 N개를 서로 공격할 수 없도록 배치하려고 합니다.
퀸은 다음 방향으로 공격할 수 있습니다.
같은 행
같은 열
같은 대각선
조건을 만족하도록 퀸 N개를 배치하는 경우의 수를 구하세요.

입력
첫째 줄에 정수 N이 주어집니다.
예시:
8

출력
퀸 N개를 서로 공격할 수 없도록 배치하는 경우의 수를 출력합니다.
예시:
92
'''

import sys
input = sys.stdin.readline

n = int(input())
count = 0
cols = [0] * n

# ----- 검사 함수
def is_valid(row):
    for prev_row in range(row):
        # 검사1. 같은 열이면 False
        if cols[prev_row] == cols[row]:
            return False
        # 검사2. 같은 대각선이면 False
        if abs(cols[row] - cols[prev_row]) == row - prev_row:
            return False
    # 문제가 없으면 True
    return True
# 검사 함수 -----

def nqueen(row):
    # 전역변수 사용을 위해
    global count
    # row == n은 0번 행부터 n-1번 행까지 퀸을 모두 놓았다는 뜻
    if row == n:
    # 조건을 만족하는 배치 하나를 찾은 것
        count += 1
        return

    for col in range(n):
        cols[row] = col
        if is_valid(row):
            nqueen(row + 1)

nqueen(0)
print(count)
