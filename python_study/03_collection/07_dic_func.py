# dictionary function
# dic.keys() : 키를 list 로 반환
dic = {'홍길동':'서울', '이순신':'충청도', '김유신':'경주'}
print(dic.keys())

# dic.values() : 값을 list 로 반환
print(dic.values())

# dic.items() : 키와 값을 list 반환
print(dic.items())

# dic.clear() : 데이터는 모두 제거함
dic.clear()

# dic.get(key) : key가 있으면 value 를 없는 None
dic = {1:'일',2:'이',3:'삼'}
print(dic.get(1))
print(dic.get(4))
# get(키 , 키값이 없을 때 출력) : None 대신 출력 됨
print(dic.get(4, "4는 키값이 아님"))

# 일반적으로 dic[key] = value 로 저장
# key 가 존재 여부에 따라 저장 하기 위해서
# dic.setdefault(key, value) 를 사용한다.
dic[3] = '셋' # 같은 키가 있으면 값이 변경 된다.
print(dic)
dic[4] = '넷'
print(dic)
dic.setdefault(4, '사') # 기존 키 값이 존재해서 저장안됨
print(dic)
dic.setdefault(5, '오') # 키 값이 없으면 저장
print(dic)

# dic.update(dic2) : 다른 dic 의 값을 추가
dic2 = {6:'육', 7:'칠'}
dic.update(dic2)
print(dic)

# 다른 dic 에 같은 키값이 있으면
# 기존 키값의 값들이 변경 된다.
dic3 = {1: '하나', 2:'둘', 8:'팔'}
dic.update(dic3)
print(dic)

# dic.pop(key) : 키에 해당 하는 키와 값을 제거
dic.pop(8)
print(dic)
dic.pop(4)
print(dic)

# fromkeys() : key, value 를 list 나 tuple 로 설정
# key 를 기준으로 value 를 반복해서 넣어준다.
key = ['name', 'age', 'address']
value = ['홍길동', 22, '서울시 종로구']
dic = dic.fromkeys(key)
print(dic)
dic = dic.fromkeys(key, value)
print(dic)

singer = {}

# key 는 이름, 구성원, 대표곡 이 된다.
singer['이름'] = input("가수 이름 입력 : ")
singer['구성원'] = input("인원 수 입력 : ")
singer['대표곡'] = input("대표곡 입력 : ")

# 키값을 이용한 singer 출력
for key in singer.keys(): # (이름, 구성원, 대표곡)
    # 이름 : 홍길동
    print(f"{key} : {singer[key]}")

# items() 는 키와 값을 반환
for key, value in singer.items():
    print(f"{key} : {value}")

menu = {}

while True:
    print("1. 메뉴 등록")
    print("2. 메뉴별 가격 보기")
    print("3. 가격 수정")
    print("4. 메뉴 삭제")
    print("0. 종료")
    select = int(input("메뉴선택 : "))

    if select == 1:
        menu_name = input("메뉴 이름 입력 : ")
        menu[menu_name] = input("가격 입력 : ")
    elif select == 2:
        for k, v in menu.items():
            print(f"{k} : {v}원")
    elif select == 3:
        name = input("수정할 메뉴 입력 : ")
        menu[name] = input("수정할 가격 입력 : ")
    elif select == 4:
        name = input("삭제할 메뉴 입력 : ")

        if menu.get(name) != None:
            menu.pop(name)
        else:
            print("검색한 메뉴가 없습니다.")
    elif select == 0:
        print("프로그램 종료")
        break
    else:
        print("선택된 메뉴가 없습니다.")