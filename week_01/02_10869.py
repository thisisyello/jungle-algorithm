'''
문제 설명
두 정수 A, B를 입력받아 아래 값을 순서대로 출력하는 문제입니다.
A + B
A - B
A x B
A ÷ B의 몫
A ÷ B의 나머지

입력 예시
7 3
출력 예시
10
4
21
2
1
'''

import sys
input = sys.stdin.readline

a, b = map(int, input().split())

answers = [
    a + b,
    a - b,
    a * b,
    a // b,
    a % b,
]

for answer in answers:
    print(answer)
