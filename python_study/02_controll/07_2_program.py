'''
은행 ATM 프로그램
- 잔고는 0 원으로 시작
1. 메뉴 : 1. 입금 2. 출금 3. 잔액조회 4. 종료
2. 입금은 음수로 입력되면 처리 되지 않고 양수만 처리한다.
3. 출금은 잔액이 부족하면 처리 되지 않는다.
4. 잔액조회는 현재 잔고만 출력한다.
5. 종료는 프로그램을 종료 한다.
------------------------------
1. 송금
2. 종료 여부 다시 물어보기
3. 비밀번호
'''

# 잔고 저장하는 변수
money = 0  # 초기값은 0 원
save_pw = '1234'  # 초기 비밀번호
bank_account = '110-110-1111'  # 계좌번호
name = '홍길동'  # 계좌 주인 이름
count = 0  # 비밀번호 틀린 횟수 저장
login_chk = False  # 로그인이 되었으면 True

# 프로그램이 시작되면 사용자가 종료를 누를때 까지 반복
while True:
    print("#" * 21)
    print("#" * 6, "KG 은행", "#" * 6)
    print("#" * 21)

    if login_chk == False:
        # 비밀번호가 맞을 때 ATM 을 사용할 수 있음
        input_pw = input("비밀번호 입력 : ")

        if save_pw == input_pw:
            print(f'{name} 님 환영합니다.')
            login_chk = True
        else:
            count += 1
            if count == 3:
                print("비밀번호 3회 틀려 프로그램을 종료합니다.")
                break
            print("비밀번호가 틀립니다. 다시 입력 하세요.")
            continue

    print("1. 입금 2. 출금 3. 잔액조회 4. 송금 9. 개인정보변경 0. 종료")
    menu = input("메뉴선택 >>> ")

    if menu == '1':  # 입금
        print("###### 입금 ######")
        tmp = int(input("입금할 금액 입력 : "))
        if tmp < 0:  # 입금할 금액이 음수 일때
            print("음수로는 입금할 수 없습니다.")
        else:  # 양수일 때
            money = money + tmp  # 잔고에 입금에 더하기
            print(f"{tmp} 원을 입금 처리 했습니다.")
            print(f"현재 잔고는 {money} 원 입니다.")

    elif menu == '2':  # 출금
        print("###### 출금 ######")
        tmp = int(input("출금할 금액 입력 : "))

        if tmp < 0:  # 음수로 입력 되었을 때
            print("음수로는 출금할 수 없습니다.")
        elif tmp > money:  # 잔고보다 큰 금액을 입력 했을 때
            print(f'출금 금액이 잔고보다 큽니다.')
        else:  # 정상적일 때
            print(f'{tmp}원을 출금 처리 했습니다.')
            # money = money - tmp
            money -= tmp  # 잔고에서 출금액 빼기
            print(f'현재 잔고는 {money} 원 입니다.')

    elif menu == '3':  # 잔액조회
        print("#### 잔액조회 ####")
        print(f"현재 잔고는 {money} 원 입니다.")

    elif menu == '4':
        print("###### 송금 ######")
        account = input("송금할 계좌 번호 입력 : ")
        if bank_account == account:
            tmp = int(input("송금할 금액 입력 : "))

            if tmp > money:
                print("송금할 금액이 부족합니다.")
            else:
                print(f"{account} 계좌로 {tmp}원을 송금합니다.")
                money -= tmp
                print(f'현재 잔고는 {money} 원 입니다.')
        else:
            print("없는 계좌번호 입니다.")

    elif menu == '9':  # 개인 정보 변경
        print("#### 개인정보변경 ####")
        input_pw = input("비밀번호 입력 : ")

        if save_pw == input_pw:
            while True:
                print("1. 이름변경 2. 비밀번호 변경 0. 메뉴로 돌아가기")
                menu = input("메뉴 선택 >>> ")

                if menu == '1':
                    print("###### 이름변경 ######")
                    name = input("변경할 이름 입력 : ")
                elif menu == '2':
                    print('#### 비밀번호변경 ####')
                    input_pw = input("비밀번호 입력 : ")

                    if save_pw == input_pw:
                        new_pw1 = input("새로운 비밀번호 입력 : ")
                        new_pw2 = input("비밀번호 다시 확인 : ")
                        if new_pw1 == new_pw2:
                            save_pw = new_pw1
                            print("비밀번호가 변경 되었습니다.")
                        else:
                            print("비밀번호 확인이 불가능 합니다.")
                    else:
                        print("비밀번호가 틀립니다. 다시 확인하세요.")
                elif menu == '0':
                    print("메인 메뉴로 돌아갑니다.")
                    break
                else:
                    print("선택된 메뉴가 없습니다.")
        else:
            print("비밀번호가 틀려 메인메뉴로 돌아갑니다.")

    elif menu == '0':  # 프로그램 종료
        while True:
            select = input("정말 종료 하시겠습니까? (y/n) ")

            if select == 'y' or select == 'Y':  # y 를 선택
                print("프로그램을 종료합니다.")
                print("KG 은행을 이용해 주셔서 감사합니다.")
                exit()  # 프로그램 종료 키워드
            elif select == 'n' or select == 'N':
                print("다시 메뉴로 돌아갑니다.")
                break  # while 문 종료 키워드
            else:
                print("다시 선택 하세요.")


    else:  # 1, 2, 3, 0 번을 제외한 번호를 입력 했을 때
        print("선택된 메뉴 번호가 없습니다.")