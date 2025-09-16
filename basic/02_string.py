#문자열은 ''나"" 모두 사용가능
name='kim ki-yeong'
content = "My Content"

# 여러줄의 문자열을 변수에 담을떼
multi = '''this is multi line string
this is second line'''
print('name:'+name)
print('content:'+content)
print('multi:'+multi)

# 문자열에 다른 타입의 데이터를 함께 출력할 경우..구번전을 신버전으로 하는 경우
age = 33

print('내 이름은 {0}이고, 나이는 {1} 입니다.'.format(name,age))
# 예전에 가장 많이 사용했었다.
print('내 이름은 ' + name+ '이고, 나이는 '+str(age)+ ' 입니다.')
# 이러한 방법도 사용했다.
print(f'내 이름은 {name}이고, 나이는 {age} 입니다.')
#요즘은 f'를 많이 사용한다.

# 여러줄 -> 한줄 처리, 한중줄-> 여러줄처럼 줄바꿈
print('이것은 한줄이지만\n 여러줄처럼 보이게 할겁니다.')
print('이것은 두줄이지만 \
한줄처럼 보이게 할겁니다.')
# \n 뉴라인이라고 해서 줄을 바꿔주는 역활을 한다.
# \는 두줄을 한줄로 인식하게 해준다.