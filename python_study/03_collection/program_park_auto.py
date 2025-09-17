# 필요한 변수
# 주차할 위치, 차량 번호

print(' 주차장 프로그램 ')
print(' 메뉴 : 1. 주차 2. 출차 3. 현황 0.종료')
# 필요한 변수

parking = [0, 0, 0, 0, 0]  # 주차구역 5개

while True:
    menu = int(input('메뉴 선택 :'))
    if menu >= 5 or menu < 0:
        print('잘못된 메뉴입니다.')
        continue
    elif menu == 1:
        car = input('차량번호를 입력해주세요')
        if car in parking:
            print('이미 주차된 차량입니다.')
            continue
        for tmp in range(len(parking)):
            if parking[tmp] == 0:
                parking[tmp] = car
                print(f'{tmp + 1}에 {car}차량이 입차되었습니다.')

                break
        else:
            print('주차자리가 없습니다.')
            break
    elif menu == 2:
        print(f'{parking}주차 현황입니다.')
        car = input('차량번호를 입력해주세요')
        if car in parking:
            print(f'{car}차량이 출차되었습니다.')
            idx = parking.index(car)
            parking[idx] = 0

            continue
        else:
            print('주차된 차량이 아닙니다.')
    elif menu == 3:
        print('주차 현황 메뉴입니다.')
        print(f'현재 주차 현황은\n{parking}입니다.')
        continue
    elif menu == 0:
        print('주차 프로그램을 종료합니다.')
        break