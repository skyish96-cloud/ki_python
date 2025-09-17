# tuple(튜플)
# - 값이 변경되지 않는 데이터의 집합
# - () 를 이용하여 tuple 을 생성한다.
# - () 는 생략 가능하다.

tp = (10,20,30)
print(tp)
print(type(tp)) # 데이터의 자료형
print(len(tp)) # tuple 안에 값의 수

# 데이터가 하나일 경우
# - () 를 사용한다고 해서 tuple이 되는 것은 아니다

tp = (10)
print(tp)
print(type(tp))


# 반드시 데이터 뒤에 , 를 사용해야 된다.
tp = (10,)
print(tp)
print(type(tp))


# ()를 생략 가능하기 때문에 생기는 현상이다.
# tp = (10) => tp = 10 : 변수 인지 튜플 인지 구분이 불가능
# tp = (10,) => tp = 10,
tp = 10,
print(tp)
print(type(tp))

# 튜플도 데이터의 자료형과 상관 없이 저장이 가능하다.
tp = 1, 10, 100, 1.234, '문자열', [1,2,3], (1,2,3)
print(tp)
print(type(tp))

# tuple 도 indexing  이 가능하다.
print(tp[0])
print(tp[1])
print(tp[2])
print(tp[3])
print(tp[4])

# tuple은 slicing 도 가능하다.
print(tp[:4])

# tuple 은 값이 변경되지 않는다.
# tp[0] = 1010 # 에러
print(tp[5])
tp[5].append(5)
print(tp[5])

# tuple 끼리 연결도 가능
tp1 = 1,2,3
tp2 = 4,5,6
tp3 = tp1 + tp2
print(tp3)

# packing 과 unpacking
# packing : tuple 을 생성하는 것을 의미
tp = 1,2,3

# unpacking : tuple 안에 값을 다른 변수로 저장
a, b, c =tp
print(a)
print(b)
print(c)

# tuple 가진 값의 갯수와 변수의 갯수가 같아야 한다.
# a,b,c,d = tp # 에러

# tuple 함수
# index() : 찾는 값의 위치 index 값을 출력
# count() : 찾는 값의 수를 세어서 출력
tp = 1,2,1,3,1,5,6
print(tp.index(1))
print(tp.count(1))