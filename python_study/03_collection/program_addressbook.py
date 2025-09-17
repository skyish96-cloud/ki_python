# 주소록 프로그램
# 이차원 list 를 이용하여 구현하세요.
# [[홍길동,010-111,주소], [이순신,010-222,주소]]
# 입력, 수정, 삭제, 전체보기, 초기화, 종료
# 입력은 이름, 전화번호, 주소 입력 받아서 저장
# 수정은 이름, 전화번호, 주소를 따로 수정할 수 있게 구현
# 삭제는 찾는 이름을 입력 받아서 삭제
# 전체보기는 저장된 모든 내역 출력
# 초기화는 전체 데이터 삭제
# 종료는 프로그램 종료

# 주소를 저장하는 list
address_book = []

while True:
    # 메뉴 출력 및 입력
    print("####### 주소록 ########")
    print("1. 입력 2. 수정 3. 삭제 4. 전체보기 5. 초기화 0. 종료")
    menu = input("메뉴 선택 : ")

    if menu == '1':
        # 새로운 list 생성 및 데이터 입력
        print("##### 주소 입력 #####")
        name = input("이름 입력 : ")
        tel = input("전화 번호 입력 : ")
        address = input("주소 입력 : ")

        # list를 새로 생성해도 되고 list 형태로 데이터를 입력해도 된다.
        address_book.append([name, tel, address])
        print(f"{name} 님의 정보가 입력되었습니다.")

    elif menu == '2':
        # 이름으로 검색 후 수정
        print('##### 주소 수정 #####')
        name = input("검색할 이름 입력 : ")

        # 직접 각 인덱스의 list 가져오는 방식
        for address in address_book:
            if address[0] == name:
                print("1. 이름 수정 2. 전화번호 수정 3. 주소 수정")
                menu = input("메뉴 선택 : ")

                if menu == '1':
                    address[0] = input("수정할 이름 입력 : ")
                    print("이름이 수정 되었습니다.")
                elif menu == '2':
                    address[1] = input("수정할 전화번호 입력 : ")
                    print("전화번호가 수정 되었습니다.")
                elif menu == '3':
                    address[2] = input("수정할 주소 입력 : ")
                    print("주소가 수정 되었습니다.")
                else:
                    print("없는 메뉴 번호 입니다.")
                break
        else:
            print(f"{name} 님의 이름을 찾을 수 없습니다.")

        '''
        # 인덱스로 직접 list 를 찾아가는 방식
        for i in range(len(address_book)):
            if address_book[i][0] == name:
                print("1. 이름 수정 2. 전화번호 수정 3. 주소 수정")
                menu = input("메뉴 선택 : ")

                if menu == '1':
                    address_book[i][0] = input("수정할 이름 입력 : ")
                    print("이름이 수정 되었습니다.")
                elif menu == '2':
                    address_book[i][1] = input("수정할 전화번호 입력 : ")
                    print("전화번호가 수정 되었습니다.")
                elif menu == '3':
                    address_book[i][2] = input("수정할 주소 입력 : ")
                    print("주소가 수정 되었습니다.")
                else:
                    print("없는 메뉴 번호 입니다.")
                break
        else:
            print(f"{name} 님의 이름을 찾을 수 없습니다.")
        '''

    elif menu == '3':
        # 이름으로 검색 후 삭제
        print('##### 주소 삭제 #####')
        name = input("검색할 이름 입력 : ")

        # 직접 각 인덱스의 list 가져오는 방식
        for address in address_book:
            if address[0] == name:
                # list 객체를 address_book에서 제거
                address_book.remove(address)
                print(f"{name} 님의 정보가 삭제 되었습니다.")
                break
        else:
            print(f"{name} 님의 이름을 찾을 수 없습니다.")
        '''
        for i in range(address_book): 
            if address_book[i][0] == name:
                # list 객체를 address_book에서 제거
                address_book.remove(address_book[i])
                # del(address_book[i])
                print(f"{name} 님의 정보가 삭제 되었습니다.")
                break
        else:
            print(f"{name} 님의 이름을 찾을 수 없습니다.")
        '''
    elif menu == '4':
        # 전체 데이터 출력
        print('##### 전체 보기 #####')
        print("이름\t전화번호\t주소")
        for address in address_book:
            print(f"{address[0]}\t{address[1]}\t{address[2]}")

        '''
        for i in range(address_book):
            print(f"{address_book[i][0]}\t{address_book[i][1]}\t{address_book[i][2]})
        '''
    elif menu == '5':
        # 전체 데이터 삭제
        print('##### 초기화 #####')
        address_book.clear()
        print("초기화가 완료 되었습니다.")

    elif menu == '0':
        # 프로그램 종료
        print('##### 프로그램 종료 #####')
        break

    else:
        print('선택된 메뉴가 없습니다.')

    print()
