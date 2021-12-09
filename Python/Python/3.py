# 제어문
score = int(input('성적을 입력 : '))

if score > 70:
    print('합격입니다')
else:
    print('불합격입니다')

score1 = int(input('국어 성적 입력 : '))
score2 = int(input('영어 성적 입력 : '))
score3 = int(input('수학 성적 입력 : '))

score_sum = score1+score2+score3
score_avg = score_sum/3

if score_avg >= 80:
    print('합격입니다')
else:
    print('불합격입니다')

import random
options = ['왼쪽', '중앙', '오른쪽']
choice = random.choice(options)
user = input('어디를 수비하겠습니까 : ')

if choice == user:
    print('성공')
else:
    print('실패')