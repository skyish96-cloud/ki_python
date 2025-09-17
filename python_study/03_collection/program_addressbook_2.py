# 주소록 프로그램
# 이차원 list 를 이용하여 구현하세요.
# 입력, 수정, 삭제, 전체보기, 초기화, 종료
# 입력은 이름, 전화번호, 주소 입력 받아서 저장
# 수정은 이름, 전화번호, 주소를 따로 수정할 수 있게 구현
# 삭제는 찾는 이름을 입력 받아서 삭제
# 전체보기는 저장된 모든 내역 출력
# 초기화는 전체 데이터 삭제
# 종료는 프로그램 종료


ls = []
stu = []
# 입력
while True:
    print('\t\t주소록 프로그램')
    print('1. 입력 2. 수정 3. 삭제 4. 전체보기 5. 초기화 0. 종료')

    menu = int(input('메뉴선택 :'))
    if 0 <= menu < 5:

        if menu == 1:
            print('입력')
            name = input('이름입력:')
            if name.isalpha():
                name = name.strip()
            else:
                print('문자만 입력해주세요.')
                continue
            tell = input('전화번호입력:')
            if not tell.isdigit():
                print('숫자만 입력해주세요.')
                continue
            add = input('주소입력:')
            stu = [name, tell, add]
            ls.append(stu)
            print(f'{name}님 정보 입력 되었습니다.')
            continue
        elif menu == 2:
            print('수정')
            print('수정할 사항 입력: 1.이름 2.번호 3.주소')
            menu_1 = int(input('수정할 메뉴 입력:'))
            if menu_1 == 1:
                print(ls)
                name = input('이름 입력:')
                if name.isalpha():
                    name_1 = input('수정할 이름 입력:')

                    if name_1.isalpha():
                        name_1 = name_1.strip()
                        for i in range(len(ls)):
                            if ls[i][0] == name:
                                ls[i][0] = name_1
                                print(f'{ls[i]}수정 완료')
                                continue

            elif menu_1 == 2:
                print(ls)
                tel = input('번호 입력:')
                if tel.isdigit():
                    tel_1 = input('수정할 번호 입력:')

                    if tel_1.isdigit():
                        for i in range(len(ls)):
                            if ls[i][1] == tel:
                                ls[i][1] = tel_1
                                print(f'{ls[i]}수정 완료')
                                break
            elif menu_1 == 3:
                print(ls)
                add = input('주소 입력:')
                add_1 = input('수정할 주소 입력:')
                for i in range(len(ls)):
                    if ls[i][2] == add:
                        ls[i][2] = add_1
                        print(f'{ls[i]}수정 완료')
                        continue
                    else:
                        print('문자만 입력')


            else:
                print('수정을 종료합니다.')
                continue
        elif menu == 3:
            print('3. 삭제')
            name = input('이름 입력:')
            if name.isalpha():
                for i in range(len(ls)):
                    if ls[i][0] == name:
                        print(f'{ls[i]}삭제 완료')
                        del (ls[i])

                        break
        elif menu == 4:
            print('전체보기')
            for i in range(len(ls)):
                print(f'{ls[i][:]}')
            continue
        elif menu == 5:
            ls.clear()
            print('초기화가 완료 되었습니다.')
        else:
            print('선택된 메뉴가 없스빈다.')
