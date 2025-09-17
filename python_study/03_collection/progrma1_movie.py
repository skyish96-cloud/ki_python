# 🧩 요구사항 (조건)
#     1.	좌석은 총 5개이며, 처음에는 모두 "빈자리"로 표시
#     2.	메뉴는 다음과 같습니다:
# 1. 좌석 예약  2. 좌석 취소  3. 좌석 현황  0. 종료

# ⸻

# ✅ 1. 좌석 예약 기능
#     •	좌석 번호(1~5)를 입력받는다
#     •	이미 예약된 자리면 "이미 예약된 좌석입니다." 출력
#     •	비어 있으면 "○번 좌석이 예약되었습니다." 출력
#     •	예약 시 "고객명"을 입력해서 좌석에 저장한다

# ⸻

# ✅ 2. 좌석 취소 기능
#     •	좌석 번호(1~5)를 입력받는다
#     •	해당 자리가 비어 있으면 "빈 자리는 취소할 수 없습니다." 출력
#     •	누가 예약했는지도 보여주고, 취소 후 "취소되었습니다." 출력

# ⸻

# ✅ 3. 좌석 현황 기능
#     •	현재 좌석의 상태를 1번부터 5번까지 차례대로 출력
# (예: [빈자리, 김철수, 빈자리, 홍길동, 빈자리])

ls = ['빈자리'] * 5

while True:

    print("메뉴 : 1. 예약 | 2. 취소 | 3. 현황 | 4. 종료")
    menu = int(input('메뉴>>>'))
    if menu >= 5 or menu < 0:
        print('없는 메뉴 입니다.')
        continue
    elif menu == 1:
        print('좌석 예약 메뉴')
        print(f'1.[{ls[0]}],2.[{ls[1]}],3.[{ls[2]}],4.[{ls[3]}],5.[{ls[4]}] 좌석 현황 입니다.')
        reserve = int(input('좌석 번호를 입력해주세요'))
        if reserve > 6 or reserve < 0:
            print('없는 좌석입니다. 정확한 번호를 입력해주세요.')
        elif ls[reserve - 1] != '빈자리':
            print('이미 예약된 좌석입니다.')
            continue
        else:
            name = (input('예약자 성함을 적어주세요 :'))
            if name.isalpha():
                print(f'{name}님예약 완료되었습니다.')
                ls[reserve - 1] = name
                continue
    elif menu == 2:
        print('좌석 취소 메뉴')
        name = input('예약자 성함을 입력해 주세요 >>>')
        if name == ls:
            if name.isalpha():
                print('성함을 정확히 입력해 주세요.')
                continue
            elif name == ls:
                ls = '빈자리'
                break

    elif menu == 3:
        print('좌석 현황')
        print(f'1.[{ls[0]}],2.[{ls[1]}],3.[{ls[2]}],4.[{ls[3]}],5.[{ls[4]}]')
    elif menu == 4:
        print('좌석 시스템 종료')
        break

