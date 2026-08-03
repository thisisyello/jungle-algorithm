'''
문제 설명
세 자리 수 두 개가 주어집니다.
두 수를 각각 거꾸로 뒤집은 뒤, 더 큰 수를 출력하세요.
예를 들어:
734 893
각 수를 뒤집으면:
437 398
이므로 더 큰 수인 437을 출력합니다.

입력
첫째 줄에 세 자리 수 두 개가 공백으로 구분되어 주어집니다.
예시:
734 893

출력
두 수를 뒤집은 뒤, 더 큰 수를 출력합니다.
예시:
437
'''

import sys
input = sys.stdin.readline

num_1, num_2 = input().split()
num_3, num_4 = "", ""

for i in range(2, -1, -1):
    num_3 += num_1[i]
    num_4 += num_2[i]

print(max(int(num_3), int(num_4)))