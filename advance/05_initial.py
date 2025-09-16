class Puppy:

    name = "" # 멤버 변수(필드) : class 안에서 사용 가능한 변수
    goal = ""

    def __init__(self,name,goal): # 생성자 : 객체화시 호출되는 함수
        # 받아온 name과 goal은 생성자를 벗어날 수 없다.(생성자의 쓰임이 다하면 함께 없어진다.)
        # 그래서 클래스(객체) 멤버에다가 넣어줘야, 객체가 살아있는 동안 사용이 가능하다.
        # 그런데 name = name형태로는 어떤 것이 객체의 멤버인지 알 수 없다.
        # 그래서 멤버인 녀석은 self를 이용하여 표시해 준다.
        self.name = name # name = name 앞에 name은 위에서 내려오고 뒤에 name은 init에서 온 name이다.
        self.goal = goal # goal = goal 앞에 goal은 위에서 내려오고 뒤에 goal은 init에서 온 goal이다.

puppy = Puppy("두부","집지키기") # __init__을 벗어날 수 없다.
print(f'이름 : {puppy.name} / 목적 : {puppy.goal}')





