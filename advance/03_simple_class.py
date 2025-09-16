# JAVA에서는 파일명 == 클래스명
# 파이썬에서는 꼭 그렇지는 않다.
class Student: # Student라는 클래스
    # - (학생과 관련된 함수 및 변수가 들어오겠구나 라고 예측이 가능)
    pass # pass는 함수나 클래스에 아무것도 없을때 오류방지를 위해 넣는 키워드

# 클래스 선언하는 방법
std1 = Student()
std2 = Student()
std3 = Student()
# 일련번호가 서로 다르다.
# 파이썬에서도 객체화는 복사를 의미하므로 서로 다른 객체는 같지 않다.
# 물론 나중에는 원본으로 사용이 가능하기도 하다.
print(std1)
print(std2)
print(std3)

# 메모리의 영역은 3가지로 나누어진다.

# STATIC영역(원본)
# HEAP영역(복사본)
# ATACK영역

# 우리는 STATIC영역(원본)을 HEAP영역(복사본)로 해서 사용하는 방식이다.
# STATIC영역은 클래스 원본이 자리잡은 곳이다.
# Class method와 class variable은 class와 같이 원본 영역에 존재한다.





