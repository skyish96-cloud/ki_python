'''
# 인적사항 프로그램
# 메뉴는 1. 입력 2. 수정 3. 삭제 4. 확인 0. 종료
# 입력 내용은 이름, 생년, 전화번호
# 수정은 이름, 생년, 전화번호 수정
# 삭제는 이름, 생년, 전화번호를 초기화
# 확인은 이름, 나이, 전화번호 출력
# 나이는 생년을 이용해서 만 나이로 출력
'''
# 기본 뼈대는 항상 이렇게 만들면 됩니다.
# while True:
#     print("#### 인적사항 ####")
#     print("1. 입력 2. 수정 3. 삭제 4. 확인 0. 종료")
#     menu = input("선택 >>> ")

#     if menu == '1':
#         print("#### 입력 ####")
#     elif menu == '2':
#         print("#### 수정 ####")
#     elif menu == '3':
#         print("#### 삭제 ####")
#     elif menu == '4':
#         print("#### 확인 ####")
#     elif menu == '0':
#         print("#### 종료 ####")
#         break
#     else:
#         print("선택된 메뉴 번호가 없습니다.")

name = ''  # 이름 저장 변수, 초기값은 없음
birth = ''  # 생년 저장 변수, 초기값은 없음
tel = ''  # 전화번호 저장 변수, 초기값은 없음

while True:
    print("#### 인적사항 ####")
    print("1. 입력 2. 수정 3. 삭제 4. 확인 0. 종료")
    menu = input("선택 >>> ")

    if menu == '1':
        print("#### 입력 ####")
        name = input("이름 입력 : ")
        name = name.replace(' ', '')

        while True:
            birth = input("생년 입력 : ")

            if birth.isdigit():
                birth = int(birth)
                break
            else:
                print("생년은 숫자만 입력 가능합니다.")

        while True:
            tel = input("전화번호 입력 : ")

            if not tel.isdigit():
                print("전화번호는 숫자만 입력 하세요.")
            elif len(tel) < 11 or len(tel) > 11:
                print("전화번호는 11자리 입니다.")
            else:
                break

        print(f"{name} 님의 정보를 저장했습니다.")

    elif menu == '2':
        print("#### 수정 ####")
        print("1. 이름 2. 생년 3. 전화번호")
        menu = input("선택 >>> ")

        if menu == '1':
            name = input("수정할 이름 입력 : ")
            name = name.replace(' ', '')
            print(f"{name} 님의 정보를 수정했습니다.")
        elif menu == '2':
            while True:
                birth = input("수정할 생년 입력 : ")

                if birth.isdigit():
                    birth = int(birth)
                    break
                else:
                    print("생년은 숫자만 입력 가능합니다.")
            print(f"{name} 님의 정보를 수정했습니다.")
        elif menu == '3':
            while True:
                tel = input("전화번호 입력 : ")

                if not tel.isdigit():
                    print("전화번호는 숫자만 입력 하세요.")
                elif len(tel) < 11 or len(tel) > 11:
                    print("전화번호는 11자리 입니다.")
                else:
                    break
            print(f"{name} 님의 정보를 수정했습니다.")

    elif menu == '3':
        print("#### 삭제 ####")

        while True:
            menu = input("삭제하시겠습니까 (y/n) ? ")

            if menu == 'y' or menu == 'Y':
                print(f'{name} 님의 정보를 삭제 했습니다.')
                name = ''
                birth = ''
                tel = ''
                break
            elif menu == 'n' or menu == 'N':
                print(f"{name} 님의 정보 삭제가 취소되었습니다.")
                break
            else:
                print("다시 입력 하세요.")


    elif menu == '4':
        print("#### 확인 ####")
        print(f"이름 : {name}")
        print(f"나이 : {2025 - birth}")
        print(f"전화번호 : {tel}")

    elif menu == '0':
        print("#### 종료 ####")
        print("프로그램을 종료 합니다.")
        break

    else:
        print("선택된 메뉴 번호가 없습니다.")