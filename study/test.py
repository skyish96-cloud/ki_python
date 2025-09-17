score = {}
while True:
    print('성적 관리 프로그램')
    print('1. 성적 등록')
    print('2. 성적 수정')
    print('3. 성적 삭제')
    print('4. 성적 검색')
    print('5. 전체 보기')
    print('0.종료')
    menu = input('메뉴 선택 : ')

    if menu == '1':
        print('성적 등록')
        name = input('이름 입력 :')
        if score.get(name) != None:
            print(f'f{name} 님은 이미 등록 되었습니다.')
            continue
        while True:
            kor = input('국어 점수 입력 : ')
            if kor.isdigit():
                kor = int(kor)
                if kor < 0 or kor > 100:
                    print('0~100사이 값만 입력하세요.')
                else:
                    break
            else:
                print('0~100사이 값만 입력하세요.')
        while True:
            eng = input('영어 점수 입력 : ')
            if eng.isdigit():
                eng = int(eng)
                if eng < 0 or eng > 100:
                    print('0~100사이 값만 입력하세요.')
                else:
                    break
            else:
                print('0~100사이 값만 입력하세요.')
        while True:
            math = input('수학 점수 입력 : ')
            if math.isdigit():
                math = int(math)
                if math < 0 or math > 100:
                    print('0~100사이 값만 입력하세요.')
                else:
                    break
            else:
                print('0~100사이 값만 입력하세요.')
        score[name] = [kor, eng, math]
        print(f'{name}님의 정보를 등록했습니다.')


    elif menu == '2':
        print('성적 수정')
        name = input('수정할 이름 입력 :')
        if score.get(name) != None:
            while True:
                kor = input('국어 점수 입력 : ')
                if kor.isdigit():
                    kor = int(kor)
                    if kor < 0 or kor > 100:
                        print('0~100사이 값만 입력하세요.')
                    else:
                        break
                else:
                    print('0~100사이 값만 입력하세요.')
            while True:
                eng = input('영어 점수 입력 : ')
                if eng.isdigit():
                    eng = int(eng)
                    if eng < 0 or eng > 100:
                        print('0~100사이 값만 입력하세요.')
                    else:
                        break
                else:
                    print('0~100사이 값만 입력하세요.')
            while True:
                math = input('수학 점수 입력 : ')
                if math.isdigit():
                    math = int(math)
                    if math < 0 or math > 100:
                        print('0~100사이 값만 입력하세요.')
                    else:
                        break
                else:
                    print('0~100사이 값만 입력하세요.')
            score[name] = [kor, eng, math]
            print(f'{name}님의 정보를 수정 등록했습니다.')
    elif menu == '3':
        print('성적 삭제')
        name = input('삭제 이름:')

        if score.get(name) != None:
            print(f'{name}님의 정보를 삭제했습니다.')
            score.pop(name)
        else:
            print(f'{name}님의 정보가 없습니다.')

    elif menu == '4':
        print('성적 검색')
        name = input('검색할 이름 입력 :')
        sum = 0
        if score.get(name) != None:
            info = score[name]
            for i in info:
                sum += i
            print(f'\t{name}')
            print(f'총점 : {sum}점')
            print(f'평균 : {sum / 3:.2f}점')

        else:
            print(f'{name}님의 정보가 없습니다.')

    elif menu == '5':
        print('전체 보기')
        if len(score) == 0:
            print('출력할 데이터가 없습니다.')
        else:
            for name, info in score.items():
                print(f'\t{name}')
                sum = 0
                for i in info:
                    sum += i
                print(f'총점 : {sum}점')
                print(f'평균 : {sum / 3:.2f}점')

    elif menu == '0':
        print('종료')
        print('프로그램을 종료합니다.')
        break
    else:
        print('선택된 메뉴가 없습니다.')
    print()
