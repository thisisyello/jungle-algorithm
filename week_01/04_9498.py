'''
문제 설명
시험 점수를 입력받아 점수에 해당하는 성적을 출력하세요.
성적 기준은 다음과 같습니다.
점수	성적
90점 이상	A
80점 이상	B
70점 이상	C
60점 이상	D
60점 미만	F

입력
시험 점수가 정수로 주어집니다.
100

출력
점수에 해당하는 성적을 출력합니다.
A
'''

import sys
input = sys.stdin.readline

score = int(input())

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
