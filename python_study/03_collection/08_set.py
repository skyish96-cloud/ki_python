# set
# - 순서가 없고 중복된 값을 처리할 수 없음
# - 집합을 처리하기 위한 데이터 자료형
# - {} 안에 값을 넣으면 set 이 된다.
#  - 딕셔너리는 {키:값} 형태로 사용된다.
#  - set은 {값,값,값} 형태로 사용한다.
# - set() 함수를 사용하면 [],{} 상관없이 set 이 된다.


set1 = set({1,2,3,})
set2 = set([1,2,3])
set3 = {1,2,3}
set4 = set()
print (f'{set1}')
print (f'{set2}')
print (f'{set3}')
print (f'{set4}')

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
# 교집합
print(set1.intersection(set2))
print(set1 & set2)
# 합집합
print(set1.union(set2))
print(set1|set2)
# 차집합
print(set1.difference(set2))
print(set1 - set2)
print(set2.difference(set1))
print(set2 - set1)

set3 = {1,2,3,4,5}

if set1 == set2:
    print('set1 과 set2 가 같다.')
if set1 == set3:
    print('set1 과 set3 가 같다')

# 같은 값이 포함되어 있는지 비교 - 같은 값이 하나도 포함되어 있지 않아야됨
set4 = { 6.7,8,9,0}

if set1.isdisjoint(set2):
    print('set1 같은 값이 포함되어 있지 않다.')
if set1.isdisjoint(set3):
    print('set3 같은 값이 포함되어 있지 않다.')
if set1.isdisjoint(set4):
    print('set4 같은 값이 포함되어 있지 않다.')

# add() : 집합에 값을 추가 한다.
set1 = {1,2,3}
set1.add(4)
print(set1)
set1.add('문자열')
print(set1)

# set1.add({'1','2','3'})
# - add 는 여러 값을 한번에 추가할 수 없다.

# update(): 여러 값을 집합에 추가한다.
set1.update({'1','2','3'})
print(set1)
set1.update(['a','b','c'])
print(set1)

# remove() : 값이 있으면 삭제하고 없으면 에러 발생한다.
set1.remove(1)
print(set1)
# set1.remove(100) # 없는 값은 에러

# discard() : 값이 있으면 삭제하고 없어도 에러가 발생하지 않음
set1.discard(2)
print(set1)
set1.discard(100) # 값이 없더라도 에러가 발생하지 않음
print(set1)

# pop() : 마지막 값을 있으면 삭제하고 없으면 에러가 발생한다.
print(set1.remove(3)) # 값 반환 없음
print(set1.discard('1')) # 값 반환 없음
print(set1.pop()) # 삭제하고 반환하기 때문에 ?(삭제한 값[임의의값이여서 바뀔수 있음])가 프린트 되었음

# clear() : 모든 값 초기화
set1.clear()
print(set1)

# set1.pop() # 비어 있는 상태에서 삭제하면 에러