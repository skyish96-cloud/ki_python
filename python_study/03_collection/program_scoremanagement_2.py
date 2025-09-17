print('\t\t성적 관리 프로그램')
dic={}
while True:
    print('메뉴 : 1.성적 등록 2.수정 3.검색 4.삭제 5.전체보기 0.종료')
    menu =input('메뉴 입력:')
    if menu =='1':
        print('1.성적 등록')
        name =  input('이름 입력 :')
        kor = int(input('국어 점수 :'))
        eng = int(input('영어 점수 :'))
        math = int(input('수학 점수 :'))
        avg = (kor+eng+math)/3
        sum = kor+eng+math
        dic[name] = {'국어':kor, '영어':eng, '수학':math, '총점':sum, '평균':avg}
        print(f'{name}님의 성적이 등록되었습니다.')
    elif menu =='2':
        print('2.수정')
        name = input('이름 입력 :')
        found = False
        for key, info in dic.items():
            if key == name:
                kor = int(input('국어 점수 :'))
                eng = int(input('영어 점수 :'))
                math = int(input('수학 점수 :'))
                avg = (kor+eng+math)/3
                sum = kor+eng+math
                print(f'{name}님의 성적이 수정되었습니다.')
                print(f'수정 결과 :{dic[key]}')
                found = True
                break
        else:
            print('등록되지 않은 이름입니다.')
    elif menu =='3':
        print('3.검색')
        name =input('검색할 이름:')
        found = False
        for key, info in dic.items():
            if key == name:
                print(f'검색결과{name}님 성적 :\n{dic[key]}')
                found =True
                break
        else:
            ('찾으시는 이름이 목록에 없습니다.')
    elif menu == '4':
        print('4.삭제')
        name = input('삭제할 이름 입력 :')
        found = False
        for key, info in dic.items():
            if key == name:
                dic.pop(key)
                print(f'{name}님의 정보가 삭제되었습니다.')
                found =True
                break
    elif menu =='5':
        print('5.전체보기')
        found = False
        for key, info in dic.items():
            print('#'*10)
            print(f'{key} : \n국어 :{info['국어']}\n영어 :{info['영어']}\n수학 :{info['수학']}\
                  \n총점 :{info['총점']}\n평균 :{info['평균']:.2f}')
            print('#'*10)
    elif menu == '0':
        print('프로그램 종료')
        break
    else:
        print('없는 메뉴입니다.')