# 입력 문자열 처리
name = '정문용'
phone = '010 - 1234 - 1234'

print(name, '의 전화번호는 ', phone, '입니다')

name = input('이름을 입력 : ')
print(name)

name = input('이름을 입력 : ')
phone = input('전화번호를 입력 : ')

print(name, '의 전화번호는 ', phone, '입니다')

a = int(input('국어 점수 입력 : '))
b = int(input('수학 점수 입력 : '))

score = a + b

print('시험 성적의 총합은 ', score, '입니다')
print('시험 성적의 평균은 ', score/2, '입니다')