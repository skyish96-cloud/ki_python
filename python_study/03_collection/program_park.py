# 주차장 프로그램
# - 5개의 공간을 가진 주차장
# - index 번호를 주차 위치로 보면 된다.
# - 자동차 번호는 숫자4자리로 하는데 문자열로 저장한다.
# - 비어 있는 공간은 '0' 으로 지정한다.
# - 프로그램을 사용자가 종료하고자 할 때 까지 반복한다.
# - 기능은 입차, 출차, 주차현황, 종료 로 지정한다.
# - 입차에서는 자동차 번호를 입력
# - 출차에서는 자동차 번호를 지우고 '0' 으로 초기화
# - 주차현황은 현재 있는 위치의 자동차 번호를 출력
# ==================================
# 추가
# - 같은 차량 번호 중복 입차 불가능


# 주차현황 및 주차위치
parking = ['0', '0', '0', '0', '0']

while True:
    print("1. 입차\n2. 출차\n3. 주차현황\n0. 종료")
    menu = input("메뉴 선택 : ")

    if menu == '1':
        print("#### 입차 ####")

        # '0' 이 빈 공간이기때문에 '0' 의 0이 되면 만차
        if parking.count('0') != 0:
            car_num = input("주차할 차량 번호 입력 : ")

            # 같은 차량 번호 중복 입차 불가능 하게 실행
            # if parking.count(car_num) == 1:
            if car_num in parking:
                print("같은 차량 번호가 존재 합니다. 다시 확인하세요.")
            # 숫자 4자리 수만 입차 허용
            elif car_num.isdigit() and len(car_num) == 4:
                for i in range(len(parking)):
                    # 빈공간이 '0' 으로 '0'을 입력한 자동차 번호로 변경
                    if parking[i] == '0':
                        parking[i] = car_num
                        break
                print(f"{car_num} 을 입차 완료 했습니다.")
            # 차량 번호 입력이 잘 못 되었을 때
            else:
                print("차량번호는 숫자4자리로 입력하세요.")
        # 주차 공간이 없을 때 (즉 '0' 이 없을 때)
        else:
            print("현재 주차 공간이 없습니다. 다른 주차장을 이용하세요.")

    elif menu == '2':
        print("#### 출차 ####")

        if parking.count('0') == 5:
            print("현재 주차 중인 차량이 없어 출차할 수 없습니다.")

        else:
            car_num = input("출차할 차량 번호 입력 : ")

            # 숫자 4자리 수만 출차 허용
            if car_num.isdigit() and len(car_num) == 4:
                for i in range(len(parking)):
                    # 입력된 자동차 번호와 동일한 차량을 찾아서 빈공간으로 변경
                    if parking[i] == car_num:
                        parking[i] = '0'  # 빈공간으로 변경
                        print(f"{car_num} 을 출차 완료 했습니다.")
                        break
                else:
                    # 같은 차량번호가 없을 때 실행
                    print(f"{car_num} 차량을 찾을 수 없습니다.")
            # 차량 번호 입력이 잘 못 되었을 때
            else:
                print("차량번호는 숫자4자리로 입력하세요.")

    elif menu == '3':
        print("#### 주차현황 ####")
        # '0' 이 5 면 전부 비어 있는 상황
        if parking.count('0') == 5:
            print("현재 주차 중인 차량이 없습니다.")

        # 차량이 하나라도 주차되어있으면 실행
        else:
            for i in range(len(parking)):
                # 비어 있는 공간일때 출력
                if parking[i] == '0':
                    print(f"{i + 1} : 비어있음")
                # 차량 번호가 있을 때 출력
                else:
                    print(f"{i + 1} : {parking[i]}")

    elif menu == '0':
        print("#### 종료 ####")
        print("프로그램을 종료합니다.")
        break
    else:
        print("선택한 메뉴 번호가 없습니다.")

    print()