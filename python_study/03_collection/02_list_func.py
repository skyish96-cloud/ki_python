# list gkatn
# - list 를 사용하기 편하게 만들어주는 기능

# append() : list 의 마지막 위치에 값을 추가 한다.
ls = []
ls.append(10)
print(ls)
ls.append(20)
print(ls)
ls.append(30)
print(ls)

# pop() L list 의 마지막 위치에 값을 삭제 한다.
# - 삭제를 하면서 삭제한 값을 반환 해 준다.
print(ls.pop())
print(ls)
print(ls.pop())
print(ls)
print(ls.pop())
print(ls)

# sort() : 오름차순으로 값을 정렬해 주는 함수
ls = [1, 5, 3, 7, 2, 4]
ls.sort()
print(ls)
# sort(reverse=True) : 내림차순으로 값을 정렬해 주는 옵션
ls.sort(reverse=True)
print(ls)

# reverse() : index 번호 역순으로 변경 해주는 함수
ls = [1, 5, 3, 7, 2, 4]
ls.reverse()
print(ls)

# ls[::-1] : index 번호 역순으로 출력 해 주는 slicing ls[첫값 끝값 -1씩]
print(ls[::-1])

# del() : list 함수는 아니지만 index 위치 값을 삭제한다.
ls = [1, 2, 3, 4, ]
del (ls[2])
print(ls)

# index() : 찾는 값의 index 번호를 반환한다.
ls = [10, 20, 10, 30]
print(ls.index(10))
print(ls.index(10, 1))

# remove() : 찾는 값의 첫번째 값을 삭제한다.
ls.remove(10)  # 찾는 값(10)의 첫번째 를 삭제함
print(ls)  # (10)이 삭제된 [20, 10, 30] 출력

# extend() : list와 list를 연결하는 함수
ls1 = [1, 2, 3]
ls2 = [4, 5, 6]
ls1.extend(ls2)  # ls1에 ls2를 추가함
print(ls1)

# clear() : list 를 초기화 하는 함수
ls1.clear()  # ls1의 리스트를 초기화
print(ls1)

