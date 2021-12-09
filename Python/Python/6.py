def add_members():
    print('신규 사용자 입력 메뉴 입니다')
    members_list.append(input('이름을 입력 : '))

def delete_members():
    print('사용자를 삭제 하는 메뉴 입니다')
    input('이름을 입력 : ')

def print_members():
    print('사용자를 출력 중 입니다')
    print(members_list)

members_list = []

print('아래 메뉴중에서 선택하세요')
print('[ 1 ] 신규 사용자 입력')
print('[ 2 ] 사용자 삭제')

menu_input = int(input('메뉴 번호 입력 : '))

if(menu_input == 1):
    add_members()
elif(menu_input == 2):
    delete_members()

print_members()