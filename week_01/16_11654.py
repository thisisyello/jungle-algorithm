'''
문제 설명
알파벳 대문자, 알파벳 소문자, 숫자 중 하나가 주어집니다.
주어진 문자의 아스키 코드 값을 출력하세요.

입력
문자 하나가 주어집니다.
예시:
A

출력
입력된 문자의 아스키 코드 값을 출력합니다.
예시:
65

다른 예시:
입력: a
출력: 97
'''

import sys
input = sys.stdin.readline

char = input().strip()

print(ord(char))