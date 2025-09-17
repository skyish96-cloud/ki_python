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

print('\t\t성적표 프로그램')
# 학번 = num
# 과목 = grade
grade = []
num = 20250001
while True:
    print('1.입력 2.수정 3.삭제 4.전체보기 0.종료')
    menu = (input('메뉴 선택 :'))
    if menu == '1':
        print('1. 입력')
        name = input('이름입력 :')
        if not name.isalpha():
            print('잘못된 이름입니다. 다시 입력해주세요.')
            continue
        kor = int(input('국어점수 입력:'))
        if not 0 < kor <= 100:
            print('0~100사이의 점수를 입력해주세요.')
            continue
        eng = int(input('영어점수 입력:'))
        if not 0 < kor <= 100:
            print('0~100사이의 점수를 입력해주세요.')
            continue
        math = int(input('수학점수 입력:'))
        if not 0 < kor <= 100:
            print('0~100사이의 점수를 입력해주세요.')
            continue
        grade.append([num, name, kor, eng, math])
        print(f'{num}번{name}님의 정보 입력이 완료 되었습니다.')

        num += 1

        continue
    elif menu == '2':
        print('2. 수정')
        print('1.이름 2.학번')
        menu2 = (input('메뉴선택:'))
        if menu2 == '1':
            name = input('이름입력 :')
            for im in grade:
                if im[1] == name:
                    print('1.국어 2.영어 3.수학')
                    cl = (input('메뉴 선택 : '))
                    if cl == '1':
                        im[2] = int(input("수정할 점수 입력 :"))
                        if not 0 < im[2] <= 100:
                            print('0~100사이의 점수를 입력해주세요.')
                            continue
                        print('국어점수 수정 완료')
                    elif cl == '2':
                        im[3] = int(input("수정할 점수 입력 :"))
                        if not 0 < im[3] <= 100:
                            print('0~100사이의 점수를 입력해주세요.')
                            continue
                        print('영어점수 수정 완료')
                    elif cl == '3':
                        im[4] = int(input("수정할 점수 입력 :"))
                        if not 0 < im[4] <= 100:
                            print('0~100사이의 점수를 입력해주세요.')
                            continue
                        print('수학점수 수정 완료')
                    else:
                        print('없는 메뉴입니다.')
                        break
                else:
                    print(f'{name}님이 없습니다.')
                    break
        elif menu2 == '2':
            num = input('학번입력:')
            if num.isdigit():
                num = int(num)
                for im in grade:
                    if (im[0]) == num:
                        print('1.국어 2.영어 3.수학')
                        cl = input('메뉴 선택:')
                        if cl == '1':
                            im[2] = int(input("수정할 점수 입력 :"))
                            if not 0 < im[2] <= 100:
                                print('0~100사이의 점수를 입력해주세요.')
                                continue
                            print('국어점수 수정 완료')
                        elif cl == '2':
                            im[3] = int(input("수정할 점수 입력 :"))
                            if not 0 < im[3] <= 100:
                                print('0~100사이의 점수를 입력해주세요.')
                                continue
                            print('영어점수 수정 완료')
                        elif cl == '3':
                            im[4] = int(input("수정할 점수 입력 :"))
                            if not 0 < im[4] <= 100:
                                print('0~100사이의 점수를 입력해주세요.')
                                continue
                            print('수학점수 수정 완료')
                        else:
                            print('없는 메뉴입니다.')
                            continue
                    else:
                        print(f'{num}학번이 검색되지 않습니다.')
                        break
            elif num.isdigit() == False:
                print('숫자만 입력해주세요')
                continue
            else:
                print('찾으시는 학번이 존재하지 않습니다.')
        else:
            print('잘못된 메뉴입니다.')
            continue
    elif menu == '3':
        print('3. 삭제')
        menu2 = (input('1.이름 2.학번'))
        if menu2 == '1':
            name = input('이름입력:')
            for im in grade:
                if im[1] == name:
                    grade.remove(im)
                    print(f'{im[0]}학번,{name}님의 정보가 삭제되었습니다')
                    break
        elif menu2 == '2':
            num = (input('학번입력: '))
            if num.isdigit():
                for im in grade:
                    if str(im[0]) == num:
                        grade.remove(im)
                        print(f'{num}학번, {im[1]}님의 정보가 삭제되었습니다.')
                        break
            else:
                ('숫자만 넣어주세요.')
                continue
        else:
            ('없는 메뉴입니다.')
            continue
    elif menu == '4':
        print('4. 전체보기')
        print('학번\t\t이름\t총점\t평균')
        for im in grade:
            print(f'{im[0]}\t{im[1]}\t{(im[2] + im[3] + im[4])}\t{(im[2] + im[3] + im[4]) / 3:.2f}\t')
        continue
    elif menu == '0':
        print('0. 종료')
        break
    else:
        print('없는 메뉴 입니다.')
        continue