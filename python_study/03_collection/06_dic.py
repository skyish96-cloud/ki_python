# Dictionary (딕셔너리)
# - key 와 value 하나의 쌍으로 가지고 있는 자료형
# - key 의 값을 통해서 value 호출하거나 저장할 수 있다.

# '이름' 과 '국어' key
# '홍길동' 과 100이 value
dic = {'이름': '홍길동', '국어': 100}
# value는 key 값을 []에 넣어서 호출
print(dic['이름'])
print(dic['국어'])

# 값 입력은 dic[key] = 값의 형식으로 저장
dic['영어'] = 100
print(dic)
print(type(dic))

site = {}
site['파이썬'] = 'http://www.python.org'
site['구글'] = 'http://www.google.com'
print(site['파이썬'])
print(site['구글'])

# 입력을 통해서 저장
info = {}

key = input("키 입력 : ")
value = input('값 입력 : ')
info[key] = value
print(key, value)

