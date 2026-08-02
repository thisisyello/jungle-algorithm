'''
문제 설명
연도를 입력받아 윤년이면 1, 윤년이 아니면 0을 출력하세요.
윤년은 다음 조건 중 하나를 만족하는 연도입니다.
4의 배수이면서 100의 배수가 아닌 연도
400의 배수인 연도

입력
연도가 정수로 주어집니다.
2000

출력
입력된 연도가 윤년이면 1, 아니면 0을 출력합니다.
1
'''

import sys
input = sys.stdin.readline

year = int(input())

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(1)
else:
    print(0)