'''
문제 설명
달팽이가 높이 V미터인 나무 막대를 올라갑니다.
달팽이는 낮에 A미터 올라가고, 밤에는 잠을 자는 동안 B미터 미끄러집니다.
단, 정상에 도착한 날에는 밤에 미끄러지지 않습니다.
달팽이가 정상에 도착하려면 며칠이 걸리는지 구하세요.

입력
첫째 줄에 세 정수 A, B, V가 공백으로 구분되어 주어집니다.
A: 낮에 올라가는 거리
B: 밤에 미끄러지는 거리
V: 나무 막대의 높이
조건:
1 ≤ B < A ≤ V ≤ 1,000,000,000
예시:
2 1 5

출력
달팽이가 정상에 도착하는 데 필요한 날짜 수를 출력합니다.
예시:
4
'''
# 주석처리 한 풀이는 시간초과..

import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())
# snail = 0
days = (v - b - 1) // (a - b) + 1

# while True:
#     snail += a
#     if snail >= v:
#         days += 1
#         break
#     snail -= b
#     days += 1

print(days)