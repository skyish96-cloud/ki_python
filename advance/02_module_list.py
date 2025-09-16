import oper

# dir() 내장 함수를 사용하면 모듈에 정의되어있는 변수, 함수 목록을 모두 볼 수 있다.
print(dir(oper))

#모듈의 이름 확인
print(oper.__name__) # 특정 모듈의 이름을 확인
print(__name__) # 현재 나의 이름 -> 현재 실행되는 함수
# (자바에서는 메인 메서드를 실행하기 위해서는 메인 메서드를 사용해야한다.
# 하지만 파이썬에서는 메인 메서드를 사용하지 않아도 메인 메서드를 실행한다.)

# class_active(활동과 관련한 함수)
# run()
# jump()
# walk()
# swim()

# class_수학적 함수
# plus()
# minus()
# multiple()
# devide()

# class_drive(운전과 관련한 함수)
# acceleration()
# break()
# drift()
