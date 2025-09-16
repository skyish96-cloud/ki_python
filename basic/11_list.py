# 파스칼 표기법 - 맨 앞글자만 대문자(JAVA의 class 생성 시 활용)
# 카멜 표기법 - 단어의 의미가 있는 첫글자를 대문자로 한다.(shopList)
# 스네이크 표기법 - 단어간의 구분을 _로 한다.(shop_list)
#    - 파이썬에서 스네이크 표기법을 제일 많이 사용



# 리스트 생성 방법 1 - 비어있는 리스트로 생성
a = []
# 파이썬에서는 크기가 없다 무한하다.

# 리스트 생성 방법 2 - 값이 있는 리스트로 생성
shop_list = ['apple','mango','carrot','banana']
print(f'shop_list : {shop_list}')

# 리스트에 값을 넣는 방법
# 가장 뒤로부터 넣는 방법
#   - 예외적으로 앞에서 들어가는 함수가 있다.
a.append(1) # 0번
a.append(2) # 1번
a.append(3) # 2번
# 특정한 번호를 지정해서 넣는 방법
a.insert(1,'X')

print(f'a의 길이 : {len(a)}')
print(f'a:{a}')

# a의 2번방에 있는 값
print(f'a[2]={a[2]}')
# a의 가장 마지막 방에 있는 값은? 4가지의 방법이 있다(*마지막은 파이썬만 허용을 해준다)
print(f'a[3]={a[3]}')
print(f'a의 마지막 방의 값은 {a[3]}')
# 길이에서  1을 뺀 값을 이용 -> 인덱스는 0번부터 시작한다는 점을 이용
# 이렇게도 가능하다.
# print(f'a의 마지막 방의 값은 {a[len(a)]}')
# - 방 번호는 0,1,2,3인데 갯수는 1,2,3,4 이고 마지막을 4로 인식해서 나올 수 없다.
# 해결방법
print(f'a의 마지막 방의 값은 {a[len(a)-1]}')
# 파이썬에서 사용되는 방식, 0보다 뒤로가면 맨 뒤로 이동된다는 개념
print(f'a의 마지막 방의 값은 {a[-1]}')

# 리스트 정렬(sort)
# - 원본을 변경하지 않는다.

shop_list.sort() # 오름차순 정렬 - 작은 수가 위로 큰 수가 밑으로
print(f'shop_list : {shop_list}')

shop_list.sort(reverse=True) # 내림차순 정렬 - 작은 수가 밑으로 큰 수가 위로
print(f'shop_list : {shop_list}')

#sorted는 원본의 리스트를 정렬한 값을 새로운 리스트로 반환한 값
new_list = sorted(shop_list)
print(f'new_list : {new_list}')

# 아스키코드를 따서 오름차순과 내림차순을 만든다.

# a의 2번 인덱에 c를 넣는다.
# insert와 다른 점은 해당 인덱스의 값을 지우고 그 자리에 들어간다는 것이다.
a[2] = 'c'
print(f'a:{a}')

# list 삭제
del a[1]
print(f'a:{a}')









