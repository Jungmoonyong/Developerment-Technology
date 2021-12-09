# 반복문
for i in range(5):
    print('for')

for i in range(1,10,1):
    print(i)

names = ['문용', '짱구', '철수', '훈이']

for name in names:
    if '문용' in names:
        print(name)

if '문용' in names:
    print(names.index('문용'))

import random

number = random.randint(1,100)

for i in range(10):
    num_input = int(input('정답 입력  : '))
    if(number > num_input):
        print('입력한 것이 작습니다')
    elif(number < num_input):
        print('입력한 것이 큽니다')
    else:
        print('정답입니다')

num = int(input('구구단 입력 : '))

i = 1

while i <= 9:
    print(num, '*', i, '=', num * i)
    i = i + 1