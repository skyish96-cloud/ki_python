# 주차장 프로그램
# - 5개의 공간을 가진 주차장
# - index 번호를 주차 위치로 보면 된다.
# - 자동차 번호는 숫자4자리로 하는데 문자열로 저장한다.
# - 비어 있는 공간은 '0'으로 지정한다.
# - 프로그램을 사용자가 종료하고자 할 때 까지 반복한다.
# - 기능은 입차, 출차, 주차현황, 종료 로 지정한다.
# - 입차에서는 자동차 번호를 입력
# - 출차에서는 자동차 번호를 지우고 '0'으로 초기화
# - 주차현황은 현재 있는 위치의 자동차 번호를 출력

print('############ 주차장 프로그램 ############')

ls = [0, 0, 0, 0, 0]  # 5개의 공간 - index 번호는 주차 위치
# 기능설명
print('1.입차 2.출차 3.주차현황 0.종료')

while True:
    menu = input('원하시는 기능의 번호를 누르세요 : ')
    if menu == '1':
        print('1. 입차 를 선택하셨습니다.')
        car_num1 = input('자동차 번호를 입력하세요 (ex:0000)')
        print('주차할 곳을 선택해주세요.')
        print(f'현재 주차상태{ls}')
        park = int(input('주차 할 곳 (좌측부터1~5):')) - 1
        if park >= 5 or park < 0:
            print('잘못된 자리를 선택하셨습니다.')
        elif ls[park] != 0:
            print('이미 주차되어있는 곳입니다. 다른곳을 선택해주세요.')
        else:
            ls[park] = car_num1
            print(f'{park + 1}자리에 {car_num1}차량 입차되었습니다.')


    elif menu == '2':
        print('2. 출차 를 선택하셨습니다.')
        print(f'현재 주차상태{ls}')
        park = int(input(f'출차를 원하시는 곳 눌러주세요.:')) - 1
        if park >= 5 or park < 0:
            print('잘못된 자리를 선택하셨습니다.')
        elif ls[park] != 0:
            print(f'{park + 1}자리에서 {ls[park]}를 출차하였습니다.')
            ls[park] = 0
        elif ls[park] == 0:
            print(f'{park + 1}자리는 비어있는 자리입니다.')



    elif menu == '3':
        print('3. 주차현황 를 선택하셨습니다.')
        print(f'현재 주차상태는\n{ls}입니다.')

    elif menu == '0':
        print('0. 종료 를 선택하셨습니다.')
        break
    else:
        print('잘못된 번호를 누르셨습니다.')
        continue


