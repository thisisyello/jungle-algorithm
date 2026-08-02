'''
문제 설명
두 자연수 A와 B를 입력받아 다음 결과를 순서대로 출력하세요.
A + B
A - B
A x B
A ÷ B의 몫
A ÷ B의 나머지

입력
첫째 줄에 두 자연수 A와 B가 공백으로 구분되어 주어집니다.
7 3

출력
덧셈, 뺄셈, 곱셈, 몫, 나머지 결과를 각각 한 줄에 하나씩 출력합니다.
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
