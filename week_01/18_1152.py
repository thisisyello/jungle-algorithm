'''
문제 설명
영어 대소문자와 공백으로 이루어진 문자열이 주어집니다.
이 문자열에 포함된 단어의 개수를 구하세요.
단어는 공백으로 구분됩니다.

입력
한 줄에 문자열이 주어집니다.
문자열의 앞이나 뒤에 공백이 있을 수도 있습니다.

예시:
The Curious Case of Benjamin Button

다른 예시:
 Mazatneunde Wae Teullyeoyo

출력
문자열에 포함된 단어의 개수를 출력합니다.
예시:
6
'''

import sys
input = sys.stdin.readline

s = input().split()

print(len(s))