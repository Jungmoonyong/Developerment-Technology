menu = {'짜장면' : 5000, '짬뽕' : 6000, '탕수육' : 12000}

menu_sum = 0

answer = '예'

while answer == '예':
    input_menu = input('메뉴를 선택 : ')
    menu_sum = menu_sum + menu[input_menu]
    answer = input('주문을 입력 : ')

print('결제 금액은 ', menu_sum)