'''
문제 설명
알파벳 소문자로 이루어진 N개의 단어가 주어집니다.
다음 조건에 따라 정렬해서 출력하세요.
길이가 짧은 것부터
길이가 같으면 사전 순으로
중복된 단어는 하나만 출력합니다.

입력
첫째 줄에 단어의 개수 N이 주어집니다.
둘째 줄부터 N개의 줄에 단어가 하나씩 주어집니다.
예시:
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours

제한
N ≤ 20,000
단어 길이 ≤ 50

출력
정렬된 단어를 한 줄에 하나씩 출력합니다.
예시:
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate
'''

import sys
input = sys.stdin.readline

n = int(input())
words = []

for _ in range(n):
    char = input().strip()
    words.append(char)

set_words = set(words)
sorted_words = sorted(set_words, key=lambda word: (len(word), word))
    
print('\n'.join(sorted_words))