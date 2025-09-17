# 호텔 프로그램
# 입실, 퇴실, 입실 현황, 종료
# 호텔 객실의 수는 처음 시작할 때 정한다.
# 입실은 비어 있는 객실만 입실 가능
# 퇴실은 입실 되어 있는 객실만 퇴실 가능
# 입실 현황은 비어 있는 객실과 입실 되어 있는 객실을 출력
# 종료는 프로그램을 종료한다.

print("###### 객실 초기 수 ######")
room_num = int(input("객실 수 입력 : "))

# 객실 수에 맞는 list 를 작성
# 비어 있으면 False, 입실되어 있으면 True 처리
room = []
for i in range(room_num):
    room.append(False)

while True:
    # 메뉴 선택창 출력
    print("######## 호텔 프로그램 #########")
    print("메뉴 : 1. 입실 2. 퇴실 3. 입실현황 0. 종료")
    # 메뉴 입력
    menu = input("메뉴 선택 : ")

    if menu == '1': # 입실 선택
        print("######### 입실 #########")
        print(f"객실 번호 : 1 ~ {len(room)}")
        select = input("입실하실 객실 번호 입력 : ")

        if select.isdigit() : # 입력받은 값이 전체 숫자로 되어 있을 때
            select = int(select) # 문자열을 정수형으로 변경
            if 1 <= select <= len(room): # 정상적인 객실 번호 입력
                if room[select - 1] == False: # 객실이 비어 있는 상태
                    room[select - 1] = True # 입실 처리
                    print(f"{select} 번 객실에 입실 완료 되었습니다.")
                else: # 객실이 입실이 되어 있는 상택
                    print(f"{select} 번 객실은 이미 입실 되어 있습니다. 다시 선택하세요.")
            else : # 객실 번호가 틀릴 경우
                print(f"{select} 번 객실은 존재 하지 않습니다. 다시 선택하세요.")
        else: # 입력 받은 값에 문자가 포함되어 있을 경우
            print("잘못된 객실 번호 입니다.")

    elif menu == '2': # 퇴실 선택
        print("######### 퇴실 #########")
        print(f"객실 번호 : 1 ~ {len(room)}")
        select = input("퇴실하실 객실 번호 입력 : ")

        if select.isdigit() : # 입력받은 값이 전체 숫자로 되어 있을 때
            select = int(select) # 문자열을 정수형으로 변경
            if 1 <= select <= len(room): # 정상적인 객실 번호 입력
                if room[select - 1] : # 객실이 입실 되어 있는 상태
                    room[select - 1] = False # 퇴실 처리
                    print(f"{select} 번 객실에 퇴실 완료 되었습니다.")
                else : # 객실이 비어 있는 상태
                    print(f"{select} 번 객실은 비어 있는 상태 입니다. 다시 선택하세요.")
            else : # 객실 번호가 틀릴 경우
                print(f"{select} 번 객실은 존재 하지 않습니다. 다시 선택하세요.")
        else: # 입력 받은 값에 문자가 포함되어 있을 경우
            print("잘못된 객실 번호 입니다.")

    elif menu == '3': # 입실 현황 선택
        print("###### 입실 현황 #######")
        print("No.\t현황")
        print("=" * 20)
        for i in range(len(room)):
            if room[i] == False: # 비어 있는 상태 출력
                print(f"{i + 1}번\t\033[32m비어있음\033[39m")
            else: # 입실 되어 있는 상태 출력
                print(f"{i + 1}번\t\033[31m입실상태\033[39m")
            '''
            ANSI 글자색
            \033[30m : 검정색
            \033[31m : 빨강색
            \033[32m : 초록색
            \033[33m : 노랑색
            \033[34m : 파랑색
            \033[35m : 분홍색
            \033[36m : 청록색
            \033[37m : 흰색
            \033[39m : 기본색
            - 배경색은 4n 으로 변경가능
            '''
        print("=" * 20)

    elif menu == '0': # 종료 선택
        print("######### 종료 #########")
        print("프로그램을 종료합니다.")
        break

    else: # 없는 메뉴 선택
        print("선택된 메뉴가 없습니다. 다시 선택하세요.")

    print("\n")