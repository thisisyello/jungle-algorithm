'''
문제 설명
각 테스트 케이스마다 학생들의 점수가 주어집니다.
학생들의 평균 점수를 구한 뒤, 평균을 넘는 학생의 비율을 백분율로 출력하세요.

입력
첫째 줄에 테스트 케이스의 개수 C가 주어집니다.
각 테스트 케이스는 한 줄로 주어지며, 첫 번째 수는 학생 수 N, 그 뒤에는 N명의 점수가 주어집니다.
예시:
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91

출력
각 테스트 케이스마다 평균을 넘는 학생의 비율을 소수점 셋째 자리까지 출력합니다.
출력 끝에는 %를 붙입니다.
예시:
40.000%
57.143%
33.333%
66.667%
55.556%
'''

import sys
input = sys.stdin.readline

c = int(input())

for _ in range(c):
    data = list(map(int, input().split()))
    n, scores = data[0], data[1:]
    avg = sum(scores) / n
    students = 0

    for score in scores:
        if score > avg:
            students += 1

    answer = students / n * 100

    print(f"{answer:.3f}%")

