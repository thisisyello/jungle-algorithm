'''
문제 설명
문자열 S와 반복 횟수 R이 주어집니다.
문자열 S의 각 문자를 R번씩 반복해서 새로운 문자열을 만든 뒤 출력하세요.
예를 들어:
R = 3
S = ABC
라면 출력은 다음과 같습니다.
AAABBBCCC

입력
첫째 줄에 테스트 케이스의 개수 T가 주어집니다.
각 테스트 케이스마다 반복 횟수 R과 문자열 S가 공백으로 구분되어 주어집니다.
예시:
2
3 ABC
5 /HTP

출력
각 테스트 케이스마다 문자열의 각 문자를 R번씩 반복한 결과를 한 줄에 하나씩 출력합니다.
예시:
AAABBBCCC
/////HHHHHTTTTTPPPPP
'''

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    r, s = input().split()
    r = int(r)
    result = ""

    for char in s:
        result += char * r

    print(result)