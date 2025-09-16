class Robot:

    # 생성자 - 객체화 할때 호출되는 함수의 일종으로
    # 객체화가 될때 가장 먼저 호출된다.
    # ex) robot이 init로 이동
    # self?(다음에)
    def __init__(self): # init는 생성자 호출
        print('Robot이 복사될때 제일 먼저 호출되는 멤버')

    def doIt(self):
        print('나는 Robot의 함수입니다.')

robot = Robot() #Robot()은 기본 생성자
robot.doIt()

# class Robot:
# 새로운 자료형, 즉 로봇이라는 타입을 정의함
# "로봇이라는 설계도"를 만든다고 생각하면 돼요

# __init__ (생성자)
# 객체를 만들 때 자동으로 호출되는 함수
# robot = Robot() 이라고 하면, 자동으로 __init__ 안에 있는 코드가 실행돼요
# * 생성자는 객체화 될 때 초기화(특정한 상태)라는 의미를 가지고 있다
# * 생성자는 객체화 될 때 초기화(특정한 상태)하는 수단으로 활용된다.
# * 초기화는 0을 만드는 것이 아니고 최초의 값을 주는 것이다.


# doIt() (일반 메서드)
# 클래스 안에서 정의한 함수 = 메서드
# robot.doIt() 으로 호출 가능

# 실행 흐름
# robot = Robot() → __init__ 실행됨
# robot.doIt() → doIt() 실행됨

# 정리
# class = 객체의 설계도
# __init__ = 객체가 생성될 때 자동 실행되는 생성자 함수
# self = 객체 자기 자신을 가리키는 예약어 (→ 다음에 꼭 다룰 부분)
# robot = Robot() → 객체 생성
# robot.doIt() → 객체의 메서드 실행