# 성적표 프로그램
# 입력, 수정, 삭제, 전체보기, 종료
# 입력
# - 학번 20250001 부터 시작하고 입력할때마다 1씩 증가
# - 이름, 국어, 영어, 수학
# 수정
# - 이름 또는 학번 검색
# - 학번, 이름은 수정 불가능, 성적만 수정 가능
# 삭제
# - 이름 또는 학번 검색으로 삭제
# - 진짜 삭제 할지도 물어보기
# 전체 보기
# - 학번 이름 총점 평균 출력
# - 평균은 소수점 2자리까지만 출력

# 학생들의 성적을 저장할 list
student_score = []
# 시작 학번
student_id = 20250001

while True:
    # 배너 및 메뉴 선택 입력 및 출력
    print("#######################")
    print("#### 성적 프로그램 ####")
    print("#######################")
    print()
    print("1. 입력 2. 수정 3. 삭제 4. 전체보기 0. 종료")
    menu = input("메뉴 선택 : ")

    if menu == '1':
        print("===== 성적 입력 =====")
        # 학번, 이름, 국어, 영어, 수학 점수 입력
        name = input("이름 입력 : ")
        kor = int(input("국어 점수 입력 : "))
        eng = int(input("영어 점수 입력 : "))
        math = int(input("수학 점수 입력 : "))

        student_score.append([student_id, kor, \
                              eng, math, kor + eng + math, (kor + eng + math) / 3])

    elif menu == '2':
        print("===== 성적 수정 =====")
        # 학번 또는 이름 검색

        # 국어, 영어, 수학 점수 수정
    elif menu == '3':
        print("===== 성적 삭제 =====")

    elif menu == '4':
        print("===== 전체 보기 =====")

    elif menu == '0':
        print("===== 프로그램 종료 =====")
        print("프로그램을 종료합니다.")
        break
    else:
        print("선택된 메뉴가 없습니다.")

    print()
