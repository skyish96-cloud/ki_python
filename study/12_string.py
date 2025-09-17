# 문자열 함수

str = 'Hello Python!!'
# upper() 와 lower() 는 검색기능에서 입력값을 처리할 때 사용
# upper() : 문자열의 영문자를 전체 대문자로 변경
print(str.upper())
# lower() : 문자열의 영문자를 전체 소문자로 변경
print(str.lower())
# swapcase() : 영문자의 대소문자를 서로 변경
print(str.swapcase())

str = 'bus station'
# title() : 영문자 단어의 첫 글자를 대문자로 변경
print(str.title())

str = 'a a b b a c b'
# count() : 찾는 문자 또는 문자열의 갯수를 출력
print(str.count('a'))
print(str.count('a a'))
# find() : 찾는 문자 또는 문자열의 시작 위치 값을 출력
print(str.find('a'))
print(str.find('a a'))
print(str.find('z'))
# rfind() : 찾는 문자 또는 문자열의 시작 위치 값을
#           오른쪽부터 검색해서 출력
print(str.rfind('a'))

# index() : find() 와 동일한 기능 하지만 없으면 에러
print(str.index('a'))
print(str.rindex('a'))
# print(str.index('z')) # 에러

str = 'banana apple'
# startswith() : 시작 문자열이 맞으면 True
print(str.startswith('ba'))
print(str.startswith('b'))
print(str.startswith('ban'))
print(str.startswith('a'))
# endswith() : 끝 문자열이 맞으면 True
print(str.endswith('e'))
print(str.endswith('ple'))
print(str.endswith('z'))

str = '      abc '
# strip() : 문자열의 양끝의 공백을 제거
# - 앞 뒤의 여러 공백도 한꺼번에 처리
print(str.strip())
# lstrip() : 문자열의 앞 공백을 제거
# rstrip() : 문자열의 뒷 공백을 제거
print(str.lstrip())
print(str.rstrip())

str = 'cat dog bird'
# replace() : 기존 문자열을 새로운 문자열로 변경
print(str.replace('cat', 'fish'))
print(str.replace('cat', ''))
print(str.replace('cat', '    '))

# split() : 공백이나 다른 문자를 기준으로 단어를 분리
print(str.split())
print(str.split('o'))

str = '''안녕하세요
반갑습니다
안녕히가세요
'''
# splitlines() : 행을 기준으로 분리
print(str.splitlines())

str1 = 'abcd'
str2 = "***"
# join() :
# str2의 문자를 str1과 반복해서 합쳐서 출력
print(str1.join(str2))

# isdigit() : 문자열이 전체 숫자면 True
str = '123'
print(str.isdigit())
str = 'abc'
print(str.isdigit())

menu = input("1. 입금 2. 출금 : ")

if menu.isdigit():
    print(int(menu))
else:
    print('숫자만 입력 가능')

# isalpha() : 문자로만 되어 있으면 True
str = 'abc'
print(str.isalpha())
str = '안녕하세요'
print(str.isalpha())
str = 'hi-fi' # 기호 안됨
print(str.isalpha())
str = 'python3' # 숫자 안됨
print(str.isalpha())

# isalnum() : 문자와 숫자로 된 문자열이면 True
str = 'abc123'
print(str.isalnum())
str = '11111'
print(str.isalnum())
str = 'abcde'
print(str.isalnum())
str = '_aaaa' # 기호만 안됨
print(str.isalnum())

# islower() : 전체 소문자로 되어 있으면 True
# isupper() : 전체 대문자로 되어 있으면 True
str = 'abc'
print(str.islower())
str = 'abc123'
print(str.islower())
str = '_abc113ㅇㅇㅇ'
print(str.islower())
str = 'Abbb' # 문자열 대문자가 포함되어 있으면 False
print(str.islower())

# isspace() : 전체 공백 문자면 True
str = 'ab '
print(str.isspace())
str = '    '
print(str.isspace())

str = ' 금 영 석 '
print(str.replace(' ', ''))

birth = '2005-09-01'
birth = birth.split('-')
age = 2025-int(birth[0])

if 7 < int(birth[1]):
    age -= 1

print (f"나이 : {age}")