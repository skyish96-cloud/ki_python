class Parent():
    def __init__(self):
        print('부모 생성자 실행!')

class Child(Parent):
    def __init__(self):
        super().__init__() # 생략된 부모 생성자
        print('자식 생성자 실행!')

ch = Child()

# 부모가 초기화가 필요 하다면 자식에게 값을 전달해서 자식이 부모에게 전달하도록 한다
class SchoolMember: # 부모
    name = ''
    age = 0

    def __init__(self, name, age): # 3. 받아온 값으로 치기화 하고 객체화 된다.
        self.name = name
        self.age = age

class Teacher(SchoolMember): # 자식
    salary = 0

    def __init__(self, name, age, salary):
        super().__init__(name, age) # 2. 부모를먼저 객체화 시키면서 초기화할 값을 전달
        self.salary = salary # 4. 그리고 나서 내각 초기화  하면서 객체화 된다.

# 1.Teacher 라는 클래스를 객체화 한다.(초기화를 위해 매개변수를 전달)
t = Teacher('김철수',33,50000000)
# 5. name 과 age 는 부모것 이지만 내것처럼 내 객체에서 가져다 쓸 수 있게 된다.
print(f'{t.name}({t.age}) - {t.salary}')

# t라는 변수에 Teacher에 변수를 입력.
# super().__init__(name, age)
# 위에 객체를 아래 부모 클래스에 입력해서 부모 객체를 불러옴
# def __init__(self, name, age):
#     self.name = name
#     self.age = age
# 위에 부모에서 받은 것으 렞외하고 salary만 자식의 객체이지만
# 부모의 객체를 상속받아서 부모의 객체를 자기 객체처럼 사용
#     def __init__(self, name, age, salary):
#     self.salary = salary


# 상속의 특징
# - 부모의 메서드의 기능이 마음에 들지 않거나 아쉬운 경우가 있다.
# - 마찬가지로 부모님께 상속받은 차가 마음에 들지 않는 경우가 있다.
#                 그럴 경우 우리는 자동차 튜닝을 한다 (Override라고 표현한다.)