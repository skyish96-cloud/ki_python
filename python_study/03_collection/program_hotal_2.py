# 호텔 프로그램
# 입실, 퇴실, 입실 현황, 종료
# 호텔 객실의 수는 처음 시작할 때 정한다.
# 입실은 비어 있는 객실만 입실 가능
# 퇴실은 입실 되어 있는 객실만 퇴실 가능
# 입실 현황은 비어 있는 객실과 입실 되어 있는 객실을 출력
# 종료는 프로그램을 종료한다.


empty = [101, 102, 103, 104, 105]
room = ''
while True:
    print('\t\t호텔 프로그램 \t\t')
    print('1. 입실 | 2. 퇴실 | 3. 입실 현황 | 0. 종료')
    menu = int(input('메뉴 선택 >>>'))

    if menu > 3 or menu < 0:
        print('없는 메뉴 입니다.')
        continue
    elif menu == 1:
        print('1. 입실')
        room = (input(f'{empty}\n비어있는 방번호를 입력해주세요'))
        if not room.isdigit():
            print('잘못 입력하셨습니다.')
            continue
        room = int(room)
        if room < 101 or room > 105:
            print('없는 객실입니다. 다시 확인하여 주세요')

        elif empty[room - 101] == f'{room}.입실':
            print('입실되어 있는 방입니다. 다른방을 선택해주세요.')
        elif empty[room - 101] == room:
            print(f'{room}에 입실되었습니다.')
            empty[room - 101] = f'{room}.입실'
            continue

    elif menu == 2:
        print('2. 퇴실')
        print(f'객실현황\n1{empty}')
        out = (input('퇴실하실 방번호를 입력하세요.:'))
        if not out.isdigit():
            print('잘못 입력하셨습니다.')
        out = int(out)

        if out < 101 or out > 105:
            print('없는 객실입니다. 다시 확인하여 주세요')

        elif empty[out - 101] == f'{out}.입실':
            print(f'{out}호 퇴실되었습니다.')
            empty[out - 101] = out
            continue
        elif empty[out - 101] == out:
            print(f'{out}호는 빈방입니다. 다른방을 선택해주세요.')
            continue

    elif menu == 3:
        print('3. 입실현황')
        print(f'{empty[:]}')
    elif menu == 0:
        print('프로그램을 종료합니다.')
        break