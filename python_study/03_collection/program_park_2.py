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
# - 자동 위치가 아닌 수동 위치로 입차
# - 요금 정산 (기본료 2시간 : 5000원, 이후 시간당 1000원)

# 주차현황 및 주차위치
parking = ['0', '0', '0', '0', '0']
parking_time = ['0', '0', '0', '0', '0']

while True:
    print("1. 입차\n2. 출차\n3. 주차현황\n0. 종료")
    menu = input("메뉴 선택 : ")

    if menu == '1':
        print("#### 입차 ####")

        # '0' 이 빈 공간이기때문에 '0' 의 0이 되면 만차
        if parking.count('0') != 0:
            # 비어 있는 공간을 알려주는 기능
            print("비어 있는 주차 공간 :", end=" ")
            for i in range(len(parking)):
                if parking[i] == '0':
                    print(i + 1, end=" ")
            print()

            while True:  # 위치의 번호가 틀리면 반복
                time = input("현재 시간 입력 : ")
                park_num = int(input("주차 위치 입력 : "))

                if park_num < 1 or park_num > 5:
                    print("잘못된 위치 번호 입니다. 다시 입력하세요.")
                else:
                    # 이미 주차된 공간이면 다시 위치 입력 받기
                    if parking[park_num - 1] != '0':
                        print("이미 다른 차량이 주차 중 입니다.")
                    else:
                        break

            car_num = input("주차할 차량 번호 입력 : ")

            # 같은 차량 번호 중복 입차 불가능 하게 실행
            # if parking.count(car_num) == 1:
            if car_num in parking:
                print("같은 차량 번호가 존재 합니다. 다시 확인하세요.")
            # 숫자 4자리 수만 입차 허용
            elif car_num.isdigit() and len(car_num) == 4:
                parking[park_num - 1] = car_num
                parking_time[park_num - 1] = time
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
            # 주차된 차량 번호 출력
            for i in range(len(parking)):
                # 비어 있는 공간일때 출력
                if parking[i] == '0':
                    print(f"{i + 1} : 비어있음")
                # 차량 번호가 있을 때 출력
                else:
                    print(f"{i + 1} : {parking[i]}")

            park_num = input("출차할 차량 위치 번호 입력 : ")

            # 숫자 4자리 수만 출차 허용
            if park_num.isdigit():
                park_num = int(park_num)

                if 1 <= park_num <= 5:
                    if parking[park_num - 1] != '0':  # 정상적인 상황
                        end_time = input("출차 시간 입력 : ")

                        start_time = parking_time[park_num - 1].split(":")
                        start_hour = start_time[0]
                        start_minute = start_time[1]

                        end_time = end_time.split(":")
                        end_hour = end_time[0]
                        end_minute = end_time[1]

                        hour = int(end_hour) - int(start_hour)
                        minute = int(end_minute) - int(start_minute)

                        if hour < 2:
                            print("요금 : 5000원")
                        else:
                            hour -= 2

                            if minute > 0:
                                print(f"{hour * 1000 + 5000 + 1000} 원")
                            else:
                                print(f"{hour * 1000 + 5000} 원")

                        print(f"{parking[park_num - 1]} 차량을 출차합니다.")
                        parking[park_num - 1] = '0'
                    else:  # 입력한 공간이 비어 있을 때
                        print("이미 비어 있는 공간 입니다. 다시 확인하세요.")
                else:  # 없는 위치 번호를 입력하거나 잘못 입력했을 때
                    print("입력하신 위치 번호는 존재하지 않습니다. 다시 확인하세요.")
            # 차량 번호 입력이 잘 못 되었을 때
            else:
                print("입력한 위치는 숫자만 가능합니다.")

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
                    print(f"{i + 1} : {parking[i]} : {parking_time[i]}")

    elif menu == '0':
        print("#### 종료 ####")
        print("프로그램을 종료합니다.")
        break
    else:
        print("선택한 메뉴 번호가 없습니다.")

    print()