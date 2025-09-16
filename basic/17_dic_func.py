dic = {
    'name':'hong,gil-dong',
    'phone':'010-1234-1234',
    'friends':['Alice','Smith','Jhone']
}


# dic.keys() : 특정한 사전의 키들만 가져와 dict_keys라는 객체를 반환한다.
print(dic.keys())
for item in dic.keys():
    print(item)

# dict_keys -> list로 변환
keys = list(dic.keys())
print(keys)

#dic.values() : 특정 사전의 값만 가져와 dict_values라는 객체를 반환
print(dic.values())
#list로 변경해서 valuse라는 변수를 담아보자
for item in dic.values(): # 딕셔너리의  values 값들을 하나씩 꺼내면서 item에 넣어줌
    print(item)

valuses = list(dic.values()) # values값을 딕셔너리에 리스트형태로 넣는다.
print(valuses)

# dic. items() : 사전의 키 : 값을 한쌍으로 가져와 dict_items로 반환한다,.
# 각 키와 값은 ()모양으로 보아 tuple 이다.
print(dic.items())
# lis로 변환해 보면 list 안에 각 키와 값이 tuple로 저장되어 있음을 알 수 있다.
li = list(dic.items())
print(li)

# 값을 가져오기
print(dic.get('name'))
print(dic['phone'])

# dic 안에 있는 모든 키와 값을 키:값 형태로 출력해보자
# 1. 키를 뽑아낸 다음, 키를 가지고 값을 뽑아내는 방법
for key in dic.keys(): # 딕셔너리의  key 값들을 하나씩 꺼내면서 key에 넣어줌
    print(f'{key}:{dic[key]}')

# 2. 키와 값을 동시에 뽑아낸 다음 거기서 키와 값을 각각 추출하는 방식
for item in dic.items():
    print(f'{item[0]}={item[1]}')

# dic은 딕셔너리,dic.items()는 (키, 값) 쌍을 튜플 형태로 꺼내준다
# item은 한번에 하나씩(키, 값) 튜플을 받는다.
# 첫번째 반복에 item = ("name", "hong,gil-dong")
# 첫번째 반복에 item = ("phone", "010-1234-1234")
# 첫번째 반복에 item = ("friends", "['Alice', 'Smith', 'Jhone']")

# 90이상인 사람의 이름만 출력
members = {
    'kim':63, 'lee':88, 'park':97, "gang":77, "hwang":100, "ga":65,
    "na":92, "la":90, "wang":100, "gu":79
}

for item in members.items():
    if item[1] >= 90:
        print(f'이름 : {item[0]}')

# key in dic : 해당 키가 사전에 존재하는지 확인

yn = 'kim' in members
print(f'kim이 있는가? = {yn}')

yn = 'jung' in members
print(f'jung이 있는가? = {yn}')

#update : 이미 있는 키면 수정을, 없는 키면 추가를 하는 함수
dic.update({'name':'홍길동','age':30,'married':False})
print(dic)

# dic.clear() : 사전 안의 내용을 모두 지운다.
dic.clear()
print(dic)