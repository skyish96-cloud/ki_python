class Car:
    def start(self):
        print('시동이 걸린다.')

    def run(self):
        print('차가 시속 50km로 달린다.')

    def stop(self):
        print('차가 멈춘다.')

class MyCar(Car):

    turbo = False

    def run(self): # 부모와 같은 메서드를 사용하면 override로 인식된다.
        if self.turbo == True:
            print('차가 시속 200km로 달린다.')
        else:
            super().run() #부모의 rum을 그대로 쓰겠다.

mc = MyCar()
mc.start()

mc.run()
mcturbo = True
mc.run()

mc.stop()

# 상석을 받으면 부모 class의 member를 내것처럼 쓸 수 있다.
# python에서는 여러 클래스를 한번에 상속 받을 수 있다.
# 상속받은 함수가 마음에 들지 않으면 바꿔 쓸 수 있다.(override)
