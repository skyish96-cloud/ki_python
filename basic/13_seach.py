# 검색 -> 특정한 자료 덩어리에서 원하는 값을 찾는것
from operator import truediv

a = [3,4,1,2,3,4,'G','F','G']
# 원하는 값에 인덱스 찾기
# 2 라는 값은 어느 위치에 있는가?
print(f'2는 어디?:{a.index(2)}')
print(f'G는 어디?:{a.index('G')}') # G는 2개지만 처음 찾은 값만 알려준다.

# 5번 인덱스부터 'G'를 찾아라
print(f'G는 어디?:{a.index('G',5)}')

# print(a.index('H'))
# ValueError: 'H' is not in list
# 값이 없으면 에러(예외)를 발생시킨다.

b = [3,4,1,2,3,4,5,6,1,3,2] # 모든 3을 찾아보세요.
print(f'3은 어디?:{b.index(3,0)}')
print(f'3은 어디?:{b.index(3,1)}')
print(f'3은 어디?:{b.index(3,5)}')

#이렇게도 방법이 있다.
# idx = b.index(3,0)
# print(f'3의 값은 {idx}번에 있다.')
# idx = b.index(3,1)
# print(f'3의 값은 {idx}번에 있다.')
# idx = b.index(3,5)
# print(f'3의 값은 {idx}번에 있다.')

idx = 0
# while True:
#     idx = b.index(3,idx)
#     print(f'3의 값은 {idx}번에 있다.')
#     idx += 1

#가장 고전적인 방법이다.
for n in b: # for in을 이용하면 list에 있는 값을 순서대로 하나씪 뽑아낸다.
    if n == 3:
      print(f'3이 있는 인덱스는 : {idx}')
    idx += 1

# 코드리뷰를 해야함...
# while True:
#     idx = b.index(3,idx)
#     print(f'3의 값은 {idx}번에 있다.')
#     idx += 1

# 리스트 요소 삭제
# del a[3] 과 a.remove(3)
# del은 특정 인덱스의 값을 지운다
# remove는 해당 값을 지운다.(한개만)
# - remove는 한개만 지우기때문에 여러번 해야한다.

print(f'a : {a}')
a.remove(3)
print(f'a : {a}')

# pop() = append()의 반대개념
# append()는 뒤에서부터 순차적으로 숫자가 붙는 개념이였다면
# pop()은 뒤에서부터 순차적으로 숫자가 빠지는 개념이다.(리스트에서 사라진다.)

val = a.pop()
print(f'빼낸 값 : {val} / a : {a}')
val = a.pop()
print(f'빼낸 값 : {val} / a : {a}')

#리스트 확장(더하기와 비슷한 개념)
print(a)
a.extend(b)
print(a)


# count(val) 특정한 값이 해당 리스트에 몇개 있는지 확인
print(a)
print(f'a 안에 3은 {a.count(4)}개 가 있다.')
print(f'a 안에 9는 {a.count(9)}개 가 있다.') # 없는 값은 0을 반환한다.

# a안에 있는 모든 3은 지워주세요.
# print(f'a : {a}')
# a.remove(3)
# print(f'a : {a}')


# 가장 많이 하는 방법
# a = [3,4,1,2,3,4,'G','F','G']
# for n in a:
#    if n == 3:
#      a.remove(3)

while True: # 조건이 무조건 참이 될 경우 계속해서 실행 되어 자동으로 멈출 수 없다.
    a.remove(3) # 3을 지우게 하는 것
    if a.count(3) == 0: # 3이 남은게 있는지 확인
        break # 3이 없으면 멈추도록 함
print(a)






