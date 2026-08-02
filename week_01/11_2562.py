'''
문제 설명
서로 다른 아홉 개의 자연수가 주어집니다.
이 중 최댓값과 그 최댓값이 몇 번째 수인지 구하세요.

입력
아홉 개의 자연수가 한 줄에 하나씩 주어집니다.
예시:
3
29
38
12
57
74
40
85
61

출력
첫째 줄에 최댓값을 출력합니다.
둘째 줄에 그 최댓값이 몇 번째 수인지 출력합니다.
예시:
85
8
'''

import sys
input = sys.stdin.readline

max_value = 0
max_index = 0

for i in range(9):
    num = int(input())

    if num > max_value:
        max_value = num
        max_index = i + 1

print(max_value)
print(max_index)